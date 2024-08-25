# 写入代码中的固定值为字面量
from sys import flags
66  # 整数字面量
print('66') # 打印输出字面量

# Number: int整数,float浮点数,complex复数,bool布尔值
n_i = 66
n_f = 6.6
n_c = 6+6j
n_b = True
t_v = type(n_c) # 获取变量类型
print(t_v)    

"""运算符: 
	+加,-减,*乘,/除,//取整,%取模,**指数
	=, +=, -=, *=, /=, %=, **=, //= """

# String: 由任意数量的字符构成
str1 = 'aaa'    # 单引号单行
str2 = "bbb"    # 双引号单行
str3 = '''字
符      
串''' # 三(单/双)引号多行
print(str3)

print(str1 + str2)				# +号拼接
print('%sccc%d' % (str1,n_i))	# 占位拼接——>"%s/%d"为占位符，表示将变量转为string/int后拼接至此处；"%"为提示符，表示其后为待拼接变量
lf = 123.456
print('%5d %.2f %7.2f' % (lf,lf,lf))	# "%5d"为转换变量为五位整数，空缺则补空格在前，超长则四舍五入
										# "%.2f"为转换变量为小数点后保留两位的浮点数
										# "%7.2f"为转换变量为总长五位、小数点后保留两位的浮点数，小数部分、整数部分、小数点均算入总长
print(f'一{type(str1)}二{666}三{n_f}')	# f:format格式化输入，使用大括号占位填入
a = 1
b= 'b'
c = 3.2
print(int(c))   # 强转int——>抹去小数
print(str(a))   # 强转string
print(float(a)) # 强转float

in_put = input('intput语句输入：')

# List: 有序的可变序列

# Tuple: 有序的不可变序列

# Set: 无序不重复集合

# Dictionary: 无需Key-Value集合




