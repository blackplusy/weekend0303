#coding=utf-8
f=open('/home/heygor/0310/test','r')
for i in f:
	print(i)
f.close()
'''
str1='heygor is handsome!!!!'
f=open('/home/heygor/0310/test3','w')
f.write(str1)
f.close()
print('finished!')
'''
f=open('/home/heygor/0310/test3','a')
f.write('\n come on baby!')
f.close()
print('yes')
