# 父子交互三种方法之 Implicit Inheritance
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent): # 继承（Inheritance）,Parent有的函数，Child继承了，可以直接用
    pass

dad = Parent()
son = Child() 

dad.implicit()
son.implicit()