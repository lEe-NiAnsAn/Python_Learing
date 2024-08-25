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

# 方法：定义与class类内的函数
