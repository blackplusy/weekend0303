#coding=utf-8
#无参数，无返回值
def hello():
	print('im your baba!')

hello()

#无参数，有返回值
def sleep():
	return 'sleep'

s=sleep()
print(s)

#有参数无返回值
def sub(x,y):
	print(x+y)

sub(2,3)

#有参数有返回值
def sub(x,y):
	return x+y
s=sub(10,20)
print(s)



