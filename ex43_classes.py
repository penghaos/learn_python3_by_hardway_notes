# 前文讲述了构建程序的过程。首先，列出所有名词、动词；其次，在这些词中筛选、合并、分类；然后，每个类别下的function

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self,secene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass
    
class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self,start_scene):
        pass

    def next_scene(self,scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

# 注：每个函数的内容都是pass，这相当于占位符，先看看这个程序的主要structure是否能运行
# 注2：有两种变成方法，一种是从上至下（top down），另一种是从下至上（bottom up），都行，都能用

