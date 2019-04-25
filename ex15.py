#ex15 

from sys import argv

script, filename = argv  # 在powershell中输入 python ex15.py ex15_sample.txt

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read()) # 这语句的意思是print( open(ex15_sample.txt).read() )

print("Type the filename again:")
file_again = input("> ") # 再输入一遍 ex15_sample.txt

# file_again = input("Type the filename again:\n>") 和上面两行语句有一样的效果

'''if file_again == 'ex15_sample.txt':
	print(open(file_again).read())
else:
	file_again = input("> ")
''' # 自己写的，不对，以后改良

txt_again = open(file_again)

print(txt_again.read())


# Hard coing 是种不好的方法，即将文件名直接写入程序，这样就无法变更想打开的文件名了。最好是从外部获得input。