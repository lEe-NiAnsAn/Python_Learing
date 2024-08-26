# 函数
def add(n1,n2):
	"""
	add函数可接收两位参数，进行打印输出并相加的操作
	:param n1: 形参n1为相加的一位数据
	:param n2: 形参n2为相加的另一位数据
	:return: 两位形参相加的和
	"""
	# 以上注释为函数说明文档
	print(f'{n1}+{n2}=')
	return n1+n2

n01 = 1
n02 = 2
print(add(n01,n02))

def noreturn():
	print('无返回值函数') 
	global gb_v # 全局变量声明
	return None # 若无return语句亦默认返回None——>逻辑判断中None等同于False

print(type(noreturn()))
none_v = None   # 变量亦可预定为None

def three_r():
	return 1,'2',3.14
x,y,z = three_r()   # 多返回值函数

def func_word(a,b,c):
	print(a,b,c)
func_word('a',c='c',b='b')  # 关键字参数——>可与位置参数混用，位置参数必须在前按位传入

def func_pre(a,b='b',c='c'):
	print(a,b,c)
func_pre('a','bb')	# 缺省参数——>靠后设置

def func_pos(*args):
	print(args)
func_pos(1,'2',3.14)		# 位置传递——>可将不定长的参数转化为元组后传入

def func_pos_w(**kwargs):
	print(kwargs)
func_pos_w(a='a',b=2,c=True)	# 关键字传递——>可将不定长的关键字参数转化为字典后传入

def func_func(func):
	print(func())
func_func(three_r)	# 函数回调

def func_lam(func,a,b):
	print(func(a,b))
func_lam(lambda n1,n2: n1 + n2,1,2)	# 匿名函数——>一次性函数，仅在此次函数调用中有效（lambda 参数:单语句函数体/返回值）



# 方法：定义与class类内的函数
