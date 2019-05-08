#父子交互三种方法之 Override Explicitly
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):
 
    def override(self): # 虽然继承了Parent的函数，但可以在自身内部重新写过该函数，即override
        print("CHILD override()")

dad = Parent()
son = Child() # son是Child的实例（instance）

dad.override()
son.override()