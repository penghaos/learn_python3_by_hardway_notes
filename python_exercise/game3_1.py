# 这个模块是战斗的过程

def battle():
    print("你碰到一个敌人")
    while True:
        action = input("'干他'or'跑路'? \n>")
        
        if action == '干他':
            print("选什么武器干他？")
            while True:
                weapon = input("'平底锅'or'板砖'or'ump9'? \n>")
                print('')
                if weapon == '平底锅':
                    print('他吃了一记平底锅，掉了30滴血。')                                                  
                    return -30
                elif weapon == '板砖':
                    print('他被板砖打得满头血，掉了50滴血。')
                    return -50
                elif weapon == 'ump9':
                    print("你用ump9把他突突了，掉了100滴血")
                    #go_on()
                    return -100
                else:
                    print("重新选择武器。")
        elif action == '跑路':
            print('在你转身跑路的那刻，一梭子弹打爆了你的头。')
            dead()

def dead():
    print("一首凉凉送给你~~~")
    exit()

