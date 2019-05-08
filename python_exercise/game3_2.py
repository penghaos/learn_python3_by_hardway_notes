# 这个模块是敌人反击的过程

from random import randint

weapons = ['平底锅','板砖','ump9']

def beat():
    action = weapons[randint(0,2)] #此处的randint包含了左右两边数字
    if action == '平底锅':
        print('对方给了你一平底锅，你掉了30滴血')
        return -30
    elif action == '板砖':
        print('你被板砖打得满头血，掉了50滴血。')
        return -50
    elif action == 'ump9':
        print("你被他用ump9突突了，掉了100滴血")           
        return -100
    else:
        print("重新选择武器。")

