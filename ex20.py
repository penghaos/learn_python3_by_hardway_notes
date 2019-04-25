
from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read()) #报错的标志在第7行和第19行
	
def rewind(f):
	f.seek(0) # http://www.runoob.com/python3/python3-file-seek.html
	
def print_a_line(line_count,f):
	print(line_count,f.readline())
	
current_file = open(input_file,'rb') #之前会报错，错误内容见文末。加上'rb'后问题解决，但字符显示不对

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file) #这个函数可以回到文本的开头

print("Let's print three lines:")

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1 # current_line += 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)#print时readline又会加上一个\n，如果不需要可在print中加入 end=""

 # 运行出错。
 #UnicodeDecodeError: 'gbk' codec can't decode byte 0xff in position 0: illegal multibyte sequence