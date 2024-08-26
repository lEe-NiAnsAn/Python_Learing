# Number: int整数,float浮点数,complex复数,bool布尔值
n_i = 66
n_f = 6.6
n_c = 6+6j
n_b = True
t_v = type(n_c) # 获取变量类型
print(t_v)    

	# 写入代码中的固定值为字面量
from sys import flags
66  # 整数字面量
print('66') # 打印输出字面量

"""运算符: 
	+加,-减,*乘,/除,//取整,%取模,**指数
	=, +=, -=, *=, /=, %=, **=, //= """
	




# String: 由任意数量的字符构成，不可修改其中字符
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

in_put = input('intput语句输入：')	# 读取键盘
print(str1[0])	# 访问字符串
print(str1[-1])	# 倒序访问
# str1[1] = b ——> 不可修改

	#字符串的常用方法
str4 = str1.replace('a','d')	# 将原字符串的所有匹配字符替换为指定字符，并返回新字符串
str5 = 'Hello World Python !'
list_str = str5.split(' ')	# 通过指定切分符切分字符串，返回一个以字符串为元素的列表
for x in list_str:
	print(x)
str6 = " HHXH H "
str7 = str6.strip(' H')	# 移除字符串首尾所有匹配的单字符，返回新字符串(如此例则' HH'与'H H'均将移除)——>未传参数则默认移除' '(空格)
n_str = str5.count('l')	# 统计指定字符串的总数
l3_str = len(str5)	# 计算字符串长度





# List: 有序的可变序列
list_none = list()	# 空列表的创建——>或list_none = []
list_none = [1,2,[3,4,5]]	# 赋值
list_n1 = [3.1,'4',1,True,list_none]	# 可存储不同数据类型的元素
print(list_n1[4][2])	# 访问嵌套列表元素
print(list_n1[-1],'\n')	# 倒序访问——>嵌套列表可直接打印输出[1,2,[3,4,5]]

	#list的常用方法：
n1_index1 = list_n1.index(3.1)	# 返回指定数据的下标
list_n1[1] = 4	# 对指定位置元素进行修改
list_n1.insert(3,5)	# 在指定位置插入新元素
list_n1.append(6)	# 尾插
list_n1.extend(list_none)	# 遍历指定容器元素逐一尾插
del list_n1[3]	# 删除指定位置元素
list_n1.pop(4)	# 移除指定位置元素
list_n1.remove(6)	# 移除与参数匹配的首个元素
list_none.clear()	# 清空列表
l1_list = len(list_n1)	# 获取列表长度

	# 遍历列表
len_n = 0
while len_n < l1_list:
	print(list_n1[len_n])
	len_n += 1	
for x in [3,4,5]:
	print(x)
print()




	
# Tuple: 有序的不可变序列
tuple_none = tuple()	# 创建空元组——>或tuple_none = ()
tuple_n1 = (1,2.3,'4',(5,6))	# 可存储不同数据类型的元素
"""注意：元组即便仅有一位元素，依然需要在其后添加“,”，否则不可识别为元组类型"""
print(tuple_n1[-1][1])	# 访问嵌套元组
n2_index = tuple_n1.index(2.3)	# 返回指定数据的下标
n_cout = tuple_n1.count(1)	# 统计元组中指定数据的总数
l2_tuple = len(tuple_n1)	# 返回元组长度

	# 遍历元组
len_n = 0
while len_n < l2_tuple:
	print(tuple_n1[len_n])
	len_n += 1	
for x in (5,6):
	print(x)
print()

tuple_list = (0,(1,2),[3,4])	
# tuple_list[0] = 1 ——> 不可修改
# tuple_list[1][1] = 3 ——> 不可修改
tuple_list[-1][1] = 14	# 允许修改元组内嵌套的列表


	# 序列：连续有序的数据容器
	# 序列的常用操作
lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = lst1[1:-2:2]	# 切片：前两位参数为确定指定序列的一个前闭后开区间，置空不填则默认为全序列；末参数为步长，默认为1即逐一取值，可置空；
print(lst2)					# 按步长在区间内切片后返回新序列
print()


# Set: 无序不重复集合
set_n1 = set()	# 声明集合	
set_n2 = {}		# 创建空集合 
set_n1 = {1,1,1,"aaa",3.14,(1,2)}	# 集合允许重复元素填入,注意：集合仅允许嵌套元组
print(set_n1)						# 但实际集合中将自动进行去重操作，且顺序将改变——>故无法使用下标访问元素
set_n1.add('b')	# 添加元素
print(set_n1)
print(set_n1.pop())	# 弹出集合中首元素，注意：每次填入数据后集合均将自动重新排序，故相当于随机访问
set_n1.clear()		# 清空集合
set_n1 = {1,2,3}
set_n2 = {3,4,5}
print(set_n1.difference(set_n2))	# 返回集合一相对集合二的补集——>{1,2}
set_n1.difference_update(set_n2)	# 集合一去除交集成为补集，集合二不做修改
print(set_n1)	# ——>{1,2}
print(set_n1.union(set_n2))		# 返回并集(依然去重)
l4_set = len(set_n2)	# 返回集合长度

	# 遍历集合
for x in set_n2:
	print(x)
i_set = 0
while i_set < l4_set:
	print(set_n2.pop())	# 逐一弹出清空集合
	i_set += 1
print(set_n2,'\n')





# Dictionary: 无序Key-Value集合
dict_n1 = dict()	# 声明字典	
dict_n2 = {}		# 创建空字典
dict_n2 = {1:'a' , '2':2 , 3.14:dict_n1 , 1:0}	# 键值与实值均可为多种数据类型，键可重复插入，字典将自动去重，
print(dict_n2)	# 插入数据后字典将自动排序										后传入的同键值数据将覆盖前数据											
print(dict_n2[1])	# 通过键访问指定元素的实值
dict_n2[2] = True	# 修改字典
dict_n2.pop('2')	# 删除字典指定元素
dict_n2.clear()	# 清空字典
dict_n1 = {1:'a',2:'b',3:'c',}
keys = dict_n1.keys()	# 获取字典中所有的键值
print(keys)
l5_dict = len(dict_n1)	# 获取字典长度

	# 字典的遍历
for x in keys:
	print(f"{x}:{dict_n1[x]}")
for key in dict_n1:			# 直接for遍历字典为遍历键值
	print(f"{key}:{dict_n1[key]}")
print()   
	
	# 容器的常用方法
set_n3 = {3,1,2,5,4}
print(max(set_n3))	# 返回容器中的最大值
print(min(set_n3))	# 返回容器中的最小值
# 各容器间的转换：list(容器)、tuple(容器)、set(容器)、str(容器)、dict(容器)
# list(dict)、tulpe(dict)、set(dict)将抛弃字典实值
# str(容器)将保留括号，即容器调用print时形式
# set(容器)时集合将自动重新排序，且将自动去重
# dict(容器)仅可转换空容器
print(sorted(set_n3))	# 升序排列
print(sorted(set_n3,reverse=True))	# 降序排列
