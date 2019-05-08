#  class 和 object 是一个东西，就像 fish 和 salmon 的关系
# salmon 是fish 的一个object
# 之后你给三条salmon取名为 Frank、Joe and Mary
# Salmon 是 Fish 的一个instance ？？(我)
# Mary 就是 salmon 的一个instance，也就是说object 是拥有Class 属性（attribute）的真实具体事物

# 总结：Fish ia a class, Salmon is a class， and Mary is an object

# Mary is a kind of salmon that is a kind of fish —— object is a class is a class

# Salmon is-a fish, salmon has-a gills

## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## ?? Dog is-a Animal
class Dog(Animal): # Dog 继承了 Animal 的函数，并且有自己的函数

    def __init__(self, name):
        ##??
        self.name = name

## ?? Cat is-a Animal
class Cat(Animal):
    
    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ##??
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## ?? Emplyee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name) # 这是个什么意思？？？
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ?? Salmon is-a Fish
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover") # 这个意思就是 一只叫“Rover”的狗；类名是Dog，object是“Rover”

## ??
satan = Cat("satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crous = Salmon()

## ??
harry = Halibut()

# Explicit is better than implicit. 清楚比含混好，写了比没写好。好的代码风格。

# 注：自己对类的理解。首先，你要定义一下‘动物’，即class Animal(object)，此处的object可以不写，但好的代码风格会写
# 注2：其次，你要定义‘猫’，猫是动物的一种，因此class Cat(Animal),这用了‘继承’的方法，Cat可以有自己的函数，同时继承了Animal的函数，即‘属性’（attribute）
# 注3：再次，你家猫叫‘cendy'，它是猫的一种，即Cat（’cendy‘），这里不是继承，而是is-a，即cendy是猫，继承了Cat的函数，记得前方没有class
# 注4：若你令cendy = Cat('cendy')，就可以调用其属性了，比如cendy.hello. cendy自己不是“类”，而是一个实例‘instance‘
