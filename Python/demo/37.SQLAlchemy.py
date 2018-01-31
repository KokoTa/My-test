# -*- coding: utf-8 -*-

from sqlalchemy import  Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random

# 创建对象基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表名
    __tablename__ = 'user'
    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建DBSession类型, DBSession对象可视为当前数据库连接
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
random_id = random.randint(1, 101)
new_user = User(id=str(random_id), name='KK')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()


# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.id=='5').one()
users = session.query(User).all()
# 打印类型和对象的name属性:
for user in users:
    print('type:', type(user))
    print('id:', user.id)
    print('name:', user.name)
# 关闭Session:
session.close()







# ORM框架也可以提供两个对象之间的一对多、多对多等功能
# class User(Base):
#     __tablename__ = 'user'

#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
#     books = relationship('Book')

# class Book(Base):
#     __tablename__ = 'book'

#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))