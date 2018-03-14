#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
print(sqlalchemy.__version__)

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/db1', echo=True)

Base = declarative_base()


# 指代一个类
class User(Base):
    # 设定表名
    __tablename__ = 'user'

    # 新增列
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), unique=True)
    password = Column(String(20))
    extra = Column(String(40))

    # 设计表
    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

    # 定义打印表内每一行内容时要显示的内容
    # 每一行都是User表的一个实例
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


# 创建表
# 将Base所有的子类（表）放入数据库中
Base.metadata.create_all(engine)

# ############增删改查############### #

# 触发sessionmaker里的__call__方法，得到一个Session实例
MySession = sessionmaker(bind=engine)
session = MySession()
# 要添加的一行数据，是一个User对象
# 插入并提交
user_row = User(name='yifei', password='123', extra='first')
session.add(user_row)
session.commit()

# 同时添加多条数据
session.add_all([
    User(name='niu', password='122', extra='second'),
    User(name='zhongshu', password='233', extra='third'),
])

# 查询,query参数是表名,没有all()方法的化，前面就sql语句，可通过print查看
session.query(User).all()
for row in session.query(User).order_by(User.id):
    print(row)
for row in session.query(User).filter(~User.name.in_(['yifei', 'niu'])):
    print(row)
session.query(User).filter(User.name == 'yifei').count()


from sqlalchemy import and_, or_
for row in session.query().filter(and_(User.name == 'yifei', User.password == '123')):
    print(row)