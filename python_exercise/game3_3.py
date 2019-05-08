# 记录双方的血量

import game3_1,game3_2

def fight(y,z):
    while y > 0 and z > 0:
        x = game3_1.battle() # 另一个module里的函数要这样用
        y = y + x
        if y > 0:
            print(f"敌人还剩{y}滴血\n")
            enemy_beat = game3_2.beat()
            z = z + enemy_beat
            if z > 0:
                print(f"你还剩{z}滴血\n")
            else:
                print("你死翘翘了。")
        else:
            print("他死翘翘了。\n")
            recover(z)

def recover(sth):
    print("战斗结束，吃点什么？")
    print("'面包'or'面条'or'车厘子'")
    food = input('> ')
    print('')
    if food == '面包':
        print("面包真好吃，恢复10点血")
        sth = sth + 10
    elif food == '面条':
        print('面条真好吃，恢复30点血')
        sth += 30
    elif food == '车厘子':
        print('车厘子真好吃（而且贵），恢复60点血')
        sth += 60
    else:
        print('瞎吃啥，没有恢复血量')
        sth += 0
    if sth > 100:
        sth = 100
    else:
        sth = sth
    print(f'你现在有{sth}滴血')
    
