#ex18 函数function

# this one is like your scripts with argv
def print_two(*args): #注意写函数的规则：def 函数名（变量1,变量2）冒号:、缩进indent
	arg1,arg2 = args #和之前接收参数的方法相同，但这不是easiest的方法
	print(f"arg1: {arg1}, arg2: {arg2}") 
	
#ok, tha *args is actually pointless, we can just do this
def print_two_again(arg1,arg2): # 这是最easy的方法
	print(f"arg1: {arg1}, arg2: {arg2}")
	
# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")
	
# this one takes no arguments
def print_none():
	print("I got nothin'.")
	
print_two("Zed","Shaw") #调用函数的写法
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

