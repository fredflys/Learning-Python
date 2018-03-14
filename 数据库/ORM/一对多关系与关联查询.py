from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/db1', echo=True)

Base = declarative_base()


class Father(Base):
    __tablename__ = 'father'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(String(16))
    # 不会出现在实际的表中
    # 加上backref属性后，Son类中可以不用再写对应的relationship语句
    son = relationship('Son', backref='father')


class Son(Base):
    __tablename__ = 'son'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(String(16))
    father_name = Column(Integer, ForeignKey('father.id'))
    # 不会出现在实际表中
    father = relationship('Father')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

f1 = Father(name='Zhang baba', age=50)
s1 = Son(name='Zhang first son', age=4)
s2= Son(name='Zhang second son', age=5)
s3 = Son(name='Zhang third son', age=)

f1.son = [s1,s2]
f1.son.append(s3)

session.add(f1)
session.commit()

# label方法用于起别名，相当于AS关键字

print(session.query(Father.name.label('father name'), Son.name.label('son name')).join(Son).all())

# filter方法的参数是条件判断，filter_by的参数则是键值对
# 这里用了relationship，直接可以获取对应的son
print(session.query(Father).filter_by(id=1).first().son)

