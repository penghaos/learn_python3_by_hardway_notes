# ex14 结合了argv和input()两种输入方法

from sys import argv

script, user_name = argv
prompt = '> ' # 将'>"赋予prompt，之后可以用prompt代替，想改变符号时，也只需改动prompt的值即可

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
