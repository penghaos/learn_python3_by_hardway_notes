

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read() # 可以用indata = open(from_file).read() 缩写为一行，缩写为这行后，就不需要in_file.close()了，python会自动关闭

print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}") # 检查文件是否存在，存在则返回TRUE；不存在，则为新建一个你输入的文件名，即d.txt
print("Ready, hit RETURN to continue, CTRL-C to ahort.")
input()

out_file = open(to_file, 'w') # 打开为'write'模式
out_file .write(indata) # 这条语句，将from_file的内容写入to_file里

print("Alright, all done.")

out_file.close() #.close() 相当于File-Save的过程
in_file.close()

# 注：echo "这是个测试文件" > test.txt 可以将“这是个测试文件”这句话替换掉test.txt中的内容
# 注：cat test.txt 可以直接在powershell中打印出test.txt的内容
