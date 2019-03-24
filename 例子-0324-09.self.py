#coding=utf-8
class student:
	def __init__(self,name):
		self.name=name
	def info(self):
		print('你的名字是%s'%self.name)

def studentinfo(s):
	s.info()

heygor=student('ladygaga')
#heygor是student类的实例化对象
#对象实例化后可以使用类的方法
studentinfo(heygor)
#studentinfo括号中传入的heygor是一个已经实例化的对象
#s.info是调用类里面的方法
#注意：函数传参可以传入常规函数，也可以传入对象

