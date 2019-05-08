# composition 不用inheritance，而是相当于调用了modules

class Other(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self): 
        self.other = Other() # 这里是重点，相当于之后的self.other 都是 other()
        # 有个问题，这里可以直接用self.other？other哪来的？？
        # 答：我做了试验，self.任何 都行

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()
