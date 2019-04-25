
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ') # 查一下 .split(' ') 的用法
	return words # output输出，即为words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words) #查一下 sorted() 的用法，应该是按字母顺序排列string
	
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0) # .pop() 的用法。此处意思应该是：删除0位置的string
	print(word)
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1) # 此处意思应该是，删除最后一个string
	print(word)
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence) # 这个函数调用了第一个函数break_words()
	return sort_words(words) # 返回值调用了第二个函数sort_words()
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words) #多个函数的调用
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence) #这里调用了倒数第3个函数
	print_first_word(words)
	print_last_word(words)

# Typing ex25. is annoying. A shortcut is to do your import like this: from ex25 import *.
# This is like saying, "Import everything from ex25." 这之后就可以直接用 原函数名，而不需要 ex25.原函数名