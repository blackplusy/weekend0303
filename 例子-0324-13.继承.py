#coding=utf-8
'''
class dog:
	def __init__(self,name,color='black'):
		self.name=name
		self.color=color
	def run(self):
		print('狗富贵，互相旺！！！')

class taidi(dog):
	def set_name(self,name):
		self.name=name
	def eat(self):
		print('im eating!!!')
gou=taidi('taitan')
print('名字是%s'%gou.name)
gou.eat()
gou.set_name('2ha')
print('旺财的新名字 %s'%gou.name)
gou.run()
'''
'''
class a:
	def printa(self):
		print('---a---')
class b:
	def printb(self):
		print('---b---')
class c(a,b):
	def printc(self):
		print('---c---')
c1=c()
c1.printa()
c1.printb()
c1.printc()
'''

class dog:
	def sayhi(self):
		print('wang!!!!')

class fadou(dog):
	def sayhi(self):
		print('aowu~~~~~~')


dog1=fadou()
dog1.sayhi()










