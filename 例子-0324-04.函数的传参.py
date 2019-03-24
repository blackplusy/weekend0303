#coding=utf-8
'''
def animal(pet2,pet1):
	print(pet1+'wang!'+pet2+'miao!!!')

#调用函数传入2个参数
animal('dog','cat')
animal('cat ','dog')
'''	
'''
def animal(pet1,pet2):
	print(pet1+'wang!'+pet2+'miao!!!')

animal(pet2='cat',pet1='2ha')
'''
'''
def animal(pet2,pet1='2ha'):
	print(pet1+' wang！'+pet2 + ' miao')

animal('heygor')
animal('jiafei','taidi')
'''

def test(x,y,*args):
        print(x,y,args)

test(1,2,'heygor','ladeng')

def test1(x,y,**args):
	print(x,y,args)
test1(1,2,a=10,b=20,c='redhair')
