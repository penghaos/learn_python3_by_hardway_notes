from sys import argv  # 没有这行语句

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ') # 此处有改动,漏了右半边)
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print() #为了美观，我加上了这行空格

script, filename = argv

txt = open(filename) # filename 写成了filenme

print(f"Here's your file {filename}:") #f" "漏了个f
print(txt.read()) # 此处漏了个t
print() #为了美观，我加上了这行空格

print("Type the filename again:")
file_again = input("> ")

print() #为了美观，我加上了这行空格

txt_again = open(file_again)

print(txt_again.read()) # 此处有改动，_改为.
print() #为了美观，我加上了这行空格

print('Let\'s practice everything.') # 此处本全为单引号' ，现将中间加上转义符\
print('You\'d need to know \'bout escapes \n with \\ that do \n newlines and \t tabs.') 
# 原来分为两行，应在第一行末尾,即escapes后加上换行符 \n

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") #没有右半边 "
print(poem)
print("--------------") # 没有左半边"
print() #为了美观，我加上了这行空格

five = 10 - 2 + 3 -  6 # 此处有改动，-后漏了数字，补上了6
print(f"This should be five: {five}") # 此处有改动，漏了右半边)

def secret_formula(started): #此处有改动，漏了冒号：
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 # 此处有改动，漏了符号，加上了 /
    return jelly_beans, jars, crates


start_point = 10000
beans, jars , crates = secret_formula(start_point) # 此处有改动，漏了crates

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # 此处有改动，漏了下划线_ ，补齐为secret_point
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
print() #为了美观，我加上了这行空格


people = 20
cats = 30 # 输入错误，将cates改为cats
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!" )# printy语句后没有打()

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # 函数后没有冒号:
    print("The world is dry!")

print() #为了美观，我加上了这行空格


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: # 函数后没有冒号:
    print("People are less than or equal to dogs.")#缺少右半边引号"


if people == dogs: # == 写成了 =
    print("People are dogs.")

print() #为了美观，我加上了这行空格