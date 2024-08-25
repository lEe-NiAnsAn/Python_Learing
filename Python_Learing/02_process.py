# 比较运算符：==, !=, >, <, >=, <=

# 生成随机数
import random
n01 = random.randint(-3,10)	# 随机生成1~10的整数

#if判断
if n01 > 2:
	print('传入值大于2')
elif n01 < 0:
	print('传入值小于0')
else:
	print('传入值不大于2亦不小于0')

