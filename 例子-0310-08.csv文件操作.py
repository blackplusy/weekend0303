#coding=utf-8
'''
import csv
with open('/home/heygor/0310/1.csv','r') as f:
	reader=csv.reader(f)
	for i in reader:
		print(i)
'''
import csv
with open('/home/heygor/0310/2.csv','w') as f:
	file=csv.writer(f,dialect='excel')
	file.writerow([1,2,3,4])
	file.writerow([5,6,7,8])
print('finished!')
