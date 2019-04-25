# list的用法

# animals = ['bear', 'tiger', 'penguin', 'zebra']
# bear = animals[0]

animals = ['bear', 'python 3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

print(animals)

# If I say "first" "second" then I using ordinal, so subtract 1. 即 第一个 则 animals[0]
# If I give you cardinal (like "The animal at 1", then use it directly. 即 animals[1]



# 第一种：用if-statement表示
"""
number = int(input("Enter a number: "))

if number <= 6 and number >=1:

#print(f"The animal in {number} which is animals{number} is ", animals[number])
#print(f"The {number}th animal which is animals[number-1] is ", animals[number-1])
# 不行，留作记录，在字符串里的animals[number]是不会变化的，被当成了字符串
	if number != 6:
		print("The animal at {} which is animals[{}] is {}".format(number,number,animals[number]))
		print("The {}th animal which is animals[{}] is {} ".format(number,number-1,animals[number-1]))
	else:
		print("There is no number at {}.".format(number))
		print("The {}th animal which is animals[{}] is {} ".format(number,number-1,animals[number-1]))
else:
	print("Your number is out of the range.")
"""
# 第二种：用while-loop表示

'''
number = int(input("Enter a number: "))

while (number <= 6 and number >=1):
	if number != 6:
		print("The animal at {} which is animals[{}] is {}".format(number,number,animals[number]))
		print("The {}th animal which is animals[{}] is {} ".format(number,number-1,animals[number-1]))
	else:
		print("There is no number at {}.".format(number))
		print("The {}th animal which is animals[{}] is {} ".format(number,number-1,animals[number-1]))
	break #不加这个break，会陷入无限循环
'''

# 第三种，用函数def表示

def lists(number):
	while (number <= 6 and number >=1):
		if number != 6:
			print("The animal at {} which is animals[{}] is {}".format(number,number,animals[number]))
			print("The {}th animal which is animals[{}] is {} ".format(number,number-1,animals[number-1]))
		else:
			print("There is no number at {}.".format(number))
			print("The {}th animal which is animals[{}] is {} ".format(number,number-1,animals[number-1]))
		break
# 调用函数，需要进入python
# 然后import ex34.py，再用ex34.lists(5)来使用
# 或者from ex34.py import * ，再用lists(5)直接使用原函数名

# 第四种，用for-loop表示

number = int(input("Enter a number: "))
for num	in range(number-1,number): #利用number-1,number 使其只循环一次。如果前者改为1，可循环number-1次吧
	if number != 6:
		print("The animal at {} which is animals[{}] is {}".format(number,number,animals[number]))
		print("The {}th animal which is animals[{}] is {} ".format(number,number-1,animals[number-1]))
	else:
		print("There is no number at {}.".format(number))
		print("The {}th animal which is animals[{}] is {} ".format(number,number-1,animals[number-1]))


# 理解第3个和处于位置3的区别

	
	
	
# 全是我写的程序，好棒！