# ex21作业：写一个formula，并写函数实现

# 目标：21 + 36 * 23 - 36 / 2 

def add(a,b):
	return a + b 
	
def subtract(a,b):
	return a - b
	
def multiply(a,b):
	return a * b
	
def divide(a,b):
	return a / b

'''second = multiply(36,23)
third = divide(36,2)

middle = subtract(second,third)
result = add(21,middle)
'''
result = add(21,subtract(multiply(36,23),divide(36,2)))

print(f"The last result is {result}.")



