#coding=utf-8
a=(1)
print(type(a))
a=(1,)
print(type(a))

a=(1,3,5)
print(a)

for i in a:
	print(i)

if 3 in a:
	print('3')


a=(1,3,5)
del a



a=(1,2,3,4,5)
print(a)
print(a[0])
print(a[-2])
print(a[2:4])
print(a[3:])
print(a[:3])

a=(1,3,4,5,3,4)
print(len(a))
print(max(a))
print(min(a))
print(a.index(5))
print(a.count(4))









