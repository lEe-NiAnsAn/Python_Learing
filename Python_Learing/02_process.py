# 比较运算符：==, !=, >, <, >=, <=

# 生成随机数
import random
n01 = random.randint(-3,6)	# 随机生成-3~6的整数

# if判断
if n01 > 2:
	print('传入值大于2')
elif n01 < 0:
	print('传入值小于0')
else:
	print('传入值不大于2亦不小于0')

# while循环
n02 = 1	
while n02 < 6:
	print(n02)
	n02+=1
print('\n')		

# for循环	
str01 = 'ABCD'
for x in str01:	# 遍历字符串
	print(x)
print('\n')

for i in range(1,7,2):	# range语句：创建前闭后开的数字区间序列——>末参数默认为1，可不填
	print(i)
print('\n')

for i in range(6):		# 若仅传入一个参数，则创建从0开始的数字序列
	print(i)
print('\n')
	
# break与continue
for i in range(10):
	if i == 4:
		break
	elif i == 2:
		continue
	else:
		print(i)