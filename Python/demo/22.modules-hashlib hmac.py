# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python常用模块 - libhash/hmac 模块
# libhash实例见文章

# hmac实例

import hmac, random
db = {}

# 获取摘要
def get_md5(key, s):
  # 传入的是bytes类型
  return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.salt = ''

  def register(self):
    if self.username in db:
      print('User in db')
      return False
    else:
      # chr 数字转字符
      self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
      self.password = get_md5(self.password, self.salt)
      self.__add_user()
      print('Registter OK')
      return True
  
  def login(self):
    userInfo = self.__get_user()
    print(userInfo)
    if userInfo != None:
      tp = get_md5(self.password, userInfo['salt']) # 求出用户输入的加盐后的摘要
      if tp != userInfo['password']:
        return False
      else:
        print('Login OK')
        return True
    else:
      print('User not found')
      return False

  def __add_user(self): # __xx 表示私有
    db[self.username] = self.__dict__ # __dict__指向__init__初始化的实例数据
    return True

  def __get_user(self):
    if self.username in db:
      return db[self.username]
    else:
      return None

def register(username, password):
    return User(username, password).register()

def login(username, password):
    return User(username, password).login()

register('bob', 'abc999')
register('alice', 'alice2008')
register('michael', '123456')
login('michael', '123456')
login('bob', 'abc999')
login('alice', 'alice2008')
