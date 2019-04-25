
# dict
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# this goes in mystuff.py
def apple():
	print("I AM APPLES!")
	
# so I can 'import mystuff.py' and use 'apple' function
import mystuff
mystuff.apple()

# put a variable named tangerine
def apple():
	print("I AM APPLES!")

tangerine = "Living reflection of a dream"

# 调用	
import mystuff

mystuff.apple()
print(mystuff.tangerine) # 知识点1：.(dot) -> mystuff.apple()

# 调用dict和mystuff.xx的异同，[key]和.key 其实本质是一样的
mystuff['apple']
mystuff.apple()
mystuff.tangerine 

# class的一个例子
class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"
	def apple(self):
		print("I AM CLASSy APPLES!")

# class 类似下面三行		
thing = MyStuff()
thing.apple()
print(thing.tangerine)

# three ways to get things from things

# dict style

mystuff['apple']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)


