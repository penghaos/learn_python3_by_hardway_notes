#这里有一张重要的图片要记，a.test("hello"),Type error ->只需要1个argument，但是给了2个

# 实际上python经常将mystuff.append('hello')转换成append(mystuff,'hello')

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_sutff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_sutff.pop() #从程序来看stuff.pop() 是将列表的最后一个字符‘剪切’下来
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")
	
print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #此处‘剪切’了stuff最后一个字符，所以少了一个
print(' '.join(stuff))
print('#'.join(stuff[3:5]))# 大多数stuff.join(x)这种格式，其实都是join(stuff,x)

# 一个概念：data structure 数据结构？
# list 就像 一叠卡片一样，作者说：
# Every concept in programming usually has some relationship to the real world


# 关于class 的教程： http://www.runoob.com/python3/python3-class.html