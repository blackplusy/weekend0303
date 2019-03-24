#coding=utf-8
def sum(a,b):
	jisuan=a+b
	return jisuan

s=sum(99,1)
print(s)

#多个返回值
def re(a,b):
	a*=10   #a=10*a
	b*=10
	return a,b
num=re(4,5)
print(num)
print(type(num))

num1,num2=re(10,40)
print(num1,num2)






