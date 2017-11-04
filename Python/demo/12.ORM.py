#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# metaclass作用：class建立需要在metaclass的基础上，用于修改类
# 可以理解成一个类创建时需要经过metaclass的初始化



# 构建ORM
# Filed保存数据库表的字段名和字段类型
class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__, self.name)
# 在Filed基础上定义各种类型
class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)') # 以父级为模板进行初始化

class IntegerField(Field):
  def __init__(self, name):
    super(IntegerField, self).__init__(name, 'bigint')

# ModelMetaclass
# cls:当前准备创建的类的对象;name:类名;bases:类继承的父类集合;attrs:类的方法集合，此例中指id/name等;
class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs): # 创建类时，数据会先在要准备创建的类中进行执行，然后传入这里处理，比如会先执行User中的IntegerField
		if name == 'Model': # 如果要创建的是Model对象，那就直接创建，不做修改
			return type.__new__(cls, name, bases, attrs) # 数据原封不动

		print('Found model: %s' % name)
		mappings = dict()
		for k, v in attrs.items(): # 此时attrs中的数据已经经过User里的IntegerField等类处理了
			if isinstance(v, Field): # 如果v值经过Field等子类的洗礼
				print('Found mapping: %s ==> %s' % (k, v))
				mappings[k] = v
		for k in mappings.keys(): # 删除传入的数据，因为数据都转义到mappings中了，就没必要保存这些数据了
			attrs.pop(k)
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		attrs['__table__'] = name # 假设表名和类名一样
		return type.__new__(cls, name, bases, attrs) # 传入修改后的attrs，创建新类

# Model
class Model(dict, metaclass=ModelMetaclass): # 继承dict
  def __init__(self, **kw): # **kw是dict的属性和方法
    super(Model, self).__init__(**kw)
  def __getattr__(self, key): # 取值，没有就报错
    try:
      return self[key]
    except KeyError:
      raise AttributeError(r"'Model' object has no attribute '%s'" % key)
  def __setattr__(self, key, value): # 设值
    self[key] = value
  def save(self): # 保存
    fields = []
    params = []
    args = []
    for k, v in self.__mappings__.items():
      fields.append(v.name) # 这个v.name很神奇
      params.append('?')
      args.append(getattr(self, k, None))
    sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
    print('SQL: %s' % sql)
    print('ARGS: %s' % str(args))

# User
class User(Model):
  # 定义属性列表，存到__mappings__后，把这里的变量都删除掉
  id = IntegerField('id') # 调用类，触发__init__和__str__，返回字符串
  name = StringField('username')
  email = StringField('email')
  password = StringField('password')
  grade = StringField('grade')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')

# 保存到数据库：
u.save()

# PS：由于继承了Model，因此u会获得Model的所有方法
print(u)
print(u.__init__)
print(u.__getattr__)
print(u.__setattr__)

# 总结：
# User首先继承了Model，而Model受ModelMetaclass约束，因此User也被约束了
# 此例中User先定义了一堆变量，然后变量经过ModelMetaclass洗礼后被删除，最后实例化User
# 由于User继承了Model，实例化过程都遵循Model的方法来做
# 然后就如你所见了0 0
