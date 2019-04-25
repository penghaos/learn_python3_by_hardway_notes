# 知识点复习

print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do:")
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-------------------------")
print(poem)
print("-------------------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars, crates # 返回了3个值
	

start_point = 10000
beans, jars, crates = secret_formula(start_point) # 三个变量，对应函数返回的三个值
#函数内的变量是暂时的，所以要用三个变量beans,jars,crates去hold 返回值

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans}, {jars} jars, and {crates} crates.")

#下面是另一种写法
start_point = start_point / 10

print("We can also do that this way.")
formula = secret_formula(start_point) #调用secret_formula函数，并返回了3个值，
print("We'd have {} beans, {} jars, nad {} crates.".format(*formula)) # 返回的三个值即*formula