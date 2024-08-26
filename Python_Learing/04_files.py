# 文件操作
"""
文件对象 = 操作函数名(name=文件名/文件路径,mode=文件操作模式,encoding=编码格式)——>默认文件路径为项目文件夹下
文件操作模式：	r：只读，默认将指针置于文件首——>需存在文件
				w：只写(覆写)，默认从文件首开始编辑，原数据将删除——>若文件不存在将自动创建文件
				a：只写(追加)，将编辑内容进行尾插——>若文件不存在将自动创建文件
"""
from ast import mod


orf = open(file="test01.txt",mode='r',encoding="UTF-8")
print(type(orf))

print(orf.read(10))     # 从指针处读取文件对象内指定长度的字符串(包括换行符)，并移动指针——>未传参则默认读取全文件
print(orf.readline())	# 从指针处读取文件对象内一行字符串(包括换行符)，并移动指针至下行首
print(orf.readlines())  # 从指针处按行全读取文件对象，返回列表(包括换行符)，并将指针移动至文件尾

orf.close()		# 关闭文件对象

orf = open(file="test01.txt",mode='r',encoding="UTF-8")
for line in orf:
	print(line)		# 按行遍历文件对象
orf.close()

with open(file="test01.txt",mode='r',encoding="UTF-8") as orf:
	print(orf.read())				# 语句块结束后自动关闭文件
	
iwf = open(file="test02.txt",mode='w',encoding="UTF-8")
iwf.write("hello")
iwf.write(" world")
iwf.write("!")	# 将字符串写入至内存中(非实际储存)
iwf.flush()		# 将内存中写入的文件刷新至实际文件中——>使得多次写入可一次性储存，节约硬盘性能
iwf.close()		# .close()同样拥有.flush()功能

iwf = open(file="test02.txt",mode='a',encoding="UTF-8")
iwf.write("\n你好")	# 追加文本数据
iwf.close()		# .close()同时执行.flush()功能

