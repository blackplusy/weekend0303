#coding=utf-8
'''
def test1():
	a=10
	print('修改前a的值是',a)
	a=20
	print('修改后a的值是',a)

def test():
	a=40
	print('test中的a是',a)

test1()
test()
'''

'''
a=100
print('a的值是',a)

def test1():
	a=20
	print('test1中的a是',a)

def test2():
	print('test2中a的值是',a)

test1()
test2()
'''

a=100
print('a的值是',a)

def test1():
	global a #声明a为全局变量
	a=200
	print('test1中修改全局变量为',a)

def test2():
	print('test2中使用全局变量',a)

test1()
test2()









