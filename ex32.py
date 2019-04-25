# list 与 for i in [x,x,x,x] 的结合
the_count = [1, 2, 3, 4, 5] # 一种新syntax，列表（list）
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dime', 3, 'quarters'] # 数字和字母混合的列表

# this first kind of for-loop goes through a list
for number in the_count: #number 不需要提前定义，for语句中已经定义
	print(f"This is count {number}")
	
# same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
	print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = [] #一个空列表

# then use the range function to do 0 to 5 counts
for i in range(0,6): #同样，右边的括号是开区间，左边是闭区间
	print(f"Adding {i} to the list.")
	# append is a function that lists understand
	elements.append(i) #往列表里append字符
	
# now we can print them out too
for i in elements:
	print(f"Element was: {i}")
	
# 2D的列表，[[1,2,3],[4,5,6]]
