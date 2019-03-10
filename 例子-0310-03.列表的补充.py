#coding=utf-8
l=[1,3,5]
print(l)
l.append('heygor')
print(l)
l.append('heygor')
print(l)
l.pop()
print(l)

l.pop()
print(l)
l.pop()
print(l)


l=['2ha','taidi','fafou','2ha']
print(l.index('2ha'))

l=[1,2,3,4,3,]
print(l.index(3))
for i in l:
	print(type(i))

for index,value in enumerate(l):
	#print(index,value)
	print('索引是:'+str(index)+' 值是：'+str(value))
print('--------------')
l1=[1,3,2,4]
print(l1)
l1.reverse()
print(l1)
l1=[1,3,2,4]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

print('**********************')
#给定列表进行操作
a=[1,2,3,4]
print([3*x for x in a])

#没有给定列表使用range方法
print([3*x for x in range(1,11)])

#加入if条件进行列表推导
print([x for x in a if x%2==0])

#多个for语句进行列表推导
print([[x,y] for x in range(2) for y in range(2)])
































