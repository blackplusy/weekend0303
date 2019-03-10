#coding=utf-8
#字符串的索引
a='hello simdia!'
print(a[3])
print(a[-2])
print(a[5])
#字符串的切片

print(a[2:])
print(a[2:6])
print(a[:-2])


name='www.baidu.com'
print(name[4:-4])


#字符串拼接
str1='python'
str2=' no.1'
print(str1+str2)

#字符串的遍历
a='heygor'
for i in a:
	print(i)

#去空格
#strip()	去除空格
#rstrip()	去除右边空格
#lstrip()	去除左边空格

a='   hello   '
print(a.strip())
print(a.rstrip())
print(a.lstrip())

#计算长度
#len()
a='simidagaga'
print(len(a))

#引号
print('heygor')
print("handsome!")

#print('i'm your baba')
print("i'm your papa")

#三引号
#注释
'''
请注意后面有人！
'''
#换行打印
print('恩1,输入帐号')
print('恩2,输入密码')

print(
'''
恩1,输入帐号
恩2,输入密码
'''
)




