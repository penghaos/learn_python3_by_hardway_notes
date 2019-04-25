# 格式化字符的用法 f" hello { variables}"

types_of_people = 10
x = f"There are {types_of_people} types of people."

f"There are {types_of_people} types of people." # 注意，这个的输出结果是字符串，即' '

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}" # 这里有个大括号

print(joke_evaluation.format(hilarious)) #格式化字符的另一种用法 .format() 

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)

