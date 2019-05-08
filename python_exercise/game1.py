# 猜数字：随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中。
from random import randint

answer = randint(100,1000)


while True:
    number = int( input("输入一个三位数字： ") )
    if number > answer:
        print("你输入的数字大了，兄弟。")
    elif number < answer:
        print("你输入的数字不够大。")
    else:
        print("花擦，猜对了！")
        break


