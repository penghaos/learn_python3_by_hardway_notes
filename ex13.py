

from sys import argv
# raad the WYSS section for how to run this 

'''script = input("enter the program: ")
first = input("enter the first argument: ")
second = input("enter the second argument: ")
third = input("enter the third argument: ")
'''# 这是我写的，想错了，外部参数只能在外部写好，内部不会影响，即如果写成python ex13.py，会报错，说无法unpack，因为只得到一个argument

script, first, second, third = argv  # ！！注意这个语句的写法

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# 使用方法是，在powershell中写 python ex13.py arg1 arg2 arg3 
# 总共4个参数： ex13.py、arg1、arg2、arg3

# 初识modules（模块），即 from sys import argv 
# 也叫 libraries