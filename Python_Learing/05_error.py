# 异常
""" 处理异常的基本语法
try:
	可能发生错误的代码
except (异常一,异常二,……) as 变量名:
	如出现异常则执行的代码
else:
	无异常执行语句
finally:
	无论是否出现异常均执行语句		
"""

try:
	print(none_str)
except NameError as N_e:		# 单个指定异常捕获
	print(f"变量未定义！{N_e}")	

	
try:
	err_n = 1/0		
	print(none_str)
except (NameError,ZeroDivisionError) as N_e:		# 多个指定异常捕获
	print(f"分母为零或变量未定义！{N_e}")		# 变量仅存储首个异常

	
try:
	err_n = 1/0		
except Exception as N_e:		# 全异常捕获
	print(f"出现异常！{N_e}")	
	

try:
	orf = open(file="test03.txt",mode='r',encoding="UTF-8")
except:		# 此处异常选择可省略，默认全异常捕获
	print("出现异常！")
	orf = open(file="test03.txt",mode='w',encoding="UTF-8")
else:
	print("该语句执行成功")	# 未出现异常
finally:
	orf.close()		# 异常处理结束语句	

def func01():
	print("func01调用")
	print(1 / 0)	# 此函数并未捕获异常
def func02():
	print("func02调用")
	func01()	# 接收异常，但此函数亦未捕获异常
def func03():
	try:
		func02()	# 接收异常并捕获
	except Exception as e:
		print(f"异常：{e}")
func03()	# 调用接收了传递异常的函数	