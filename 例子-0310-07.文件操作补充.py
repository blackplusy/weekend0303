#coding=utf-8
file=open('/home/heygor/0310/txl.txt','r')
for i in file.readlines():
	#print(i)
	#print(type(i))
	i=i.strip('\n')
	i=i.split(' ')
	#print(i)
	if i[-1]=='110':
		print('yes')
		break
	else:
		print('not here')
file.close()
