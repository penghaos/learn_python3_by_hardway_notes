# ex19的作业 自己编一个函数

# 目标：编一个函数，有2个变量，变量由用户输入，可以输入字符串或数字，按ctrl-z结束

def peng(x,y):
	print("Caluting", end = ' ')
	print("*"*10)
	print(f"The sum of two numbers is: { x + y }")
	print(f"The differ of two numbers is: { x - y}")
	
first = int(input(f"Input the first numuber: "))
second = int(input(f"Input the second numuber: "))
peng(first,second)
	

# 可运行。问题是无法验证用户的输入类型，如果输入字符串，则报错。
# 想检验用户输入的是否是数字，要用到if语句，以及验证是否为数字的函数，以后学。