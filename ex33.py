# while-loop
# while-loop 可能无限循环，因此 1. 也许用for-loop好一些；2、确保while的布尔值会变成False；
# while True 可无限循环，在循环用上break 或 exit(0) 见ex35.py

i = 0
numbers = []
times = int(input("input a number: ")) #作业题

#while i < 6:
while i < times: #作业题部分
	print(f"At the top i is {i}")
	numbers.append(i)
	
	i = i + 1
	print("Numbers now:", numbers)
	print(f"At the bottom i is {i}")
	
	print("The numbers:")
	
	for num in numbers:
		print(num)

# 在python内调用ex33.py时，输入 import ex33
# 而不是 import ex33.py，否则会出错		