import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, UniqueConstraint,Index
from sqlalchemy.orm import sessionmaker, relationships

Base = declarative_base()


def session():
    engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/db3', echo=True)
    MySession = sessionmaker(bind=engine)
    session = MySession()
    return session

# 一张表对应一个类
# 用户信息表，包含ID，用户名，密码，邮箱，创建时间，共5个域
class UserInfo(Base):
    # 把表名赋给静态字段
    __tablename__ = 'userinfo'
    # 序号nid，用户名username，密码password，邮箱email，创建时间ctime
    # 一行数据就是一个对象
    nid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))
    password = Column(String(32))
    email = Column(String(32))
    ctime = Column(TIMESTAMP)

    # 建立组合索引，这里是方便在登陆采用不同的登陆方式也能更好的索引数据库
    # 用户名+密码   和   邮箱+密码   两种组合索引
    __table_args__ = (
        Index('ix_user_pwd', 'username', 'password'),
        Index('ix_email_pwd', 'email', 'password'),
    )


# 信息类型表
class NewsType(Base):
    __tablename__ = 'newstype'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(32))


# 信息表，包含信息ID，用户ID（外键），信息类型（外键），创建时间，标题，URL，内容，共7个域
class News(Base):
    __tablename__ = 'news'

    nid = Column(Integer, primary_key=True, autoincrement=True)
    # 建立外键---两个
    user_info_id = Column(Integer, ForeignKey("userinfo.nid"))
    news_type_id = Column(Integer, ForeignKey("newstype.nid"))
    ctime = Column(TIMESTAMP)
    title = Column(String(32))
    url = Column(String(128))
    content = Column(String(150))


# 点赞表，包含ID，点赞者ID（外键），信息ID（外键），创建时间
class Favor(Base):
    __tablename__ = 'favor'

    nid = Column(Integer, primary_key=True, autoincrement=True)
    # 点赞者id
    user_info_id = Column(Integer, ForeignKey("userinfo.nid"))
    # 信息id
    news_id = Column(Integer, ForeignKey("news.nid"))
    ctime = Column(TIMESTAMP)

    # 建立联合唯一索引
    __table_args__ = (
        UniqueConstraint('user_info_id', 'news_id', name='uix_uid_nid'),
    )


# 评论表，包含ID，用户ID（外键），信息ID（外键），回复者ID，赞（数字），踩（数字），发布设备，发布内容
class Comment(Base):
    __tablename__ = 'comment'

    nid = Column(Integer, primary_key=True, autoincrement=True)
    # 评论者id
    user_info_id = Column(Integer, ForeignKey("userinfo.nid"))
    # 评论的信息id
    news_id = Column(Integer, ForeignKey("news.nid"))
    # 如果为None，就是评论文章，如果是数字就是回复某个人
    reply_id = Column(Integer, ForeignKey("comment.nid"), nullable=True, default=None)
    # 顶一下
    up = Column(Integer)
    # 踩一下
    down = Column(Integer)
    # 创建时间
    ctime = Column(TIMESTAMP)
    # 发表设备：手机，电脑，苹果....
    device = Column(String(32))
    # 发表内容
    content = Column(String(150))


# 往邮箱发送验证码时用到的临时表
class SendCode(Base):
    __tablename__ = "sendcode"

    # 注册时验证码信息
    nid = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(32), index=True)
    code = Column(String(6))
    # status = Column(Integer)  #状态码，0表示未注册，1成功，2拉黑
    # 验证码的有效时间
    stime = Column(TIMESTAMP)  # 发送时间



