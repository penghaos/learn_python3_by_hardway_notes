# 你想做个清新脱俗的文字游戏，只在命令行的黑框里运行。

# 要有战斗模式，主角有HP属性，战斗和吃东西会对HP有相应的增减效果。
# 功能描述：尽量参考回合制RPG游戏的模式，游戏剧情自编，

#主程序

import game3_1,game3_2,game3_3

class Person(object):
    def __init__(self,name):
        self.name = name
    def blood(self):
        return 100  #函数要有返回值，这里卡住了很久

you = Person('peter')
enemy = Person('bob')

y = enemy.blood() # 这里卡住过
z = you.blood()

game3_3.fight(y,z) # 调用game3_3中的fight函数，作用是记录战斗过程
