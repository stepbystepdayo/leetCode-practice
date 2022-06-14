# How to make class

# class Person: # fist char need to capital.
#     def __init__(self,x): # x is inisilizing (初期化するために必要) 
#         print(x)

# p1 = Person(2) # inside() we need to put x の値 output is 2
# p2 = Person(3)  # 3


# print(p1) #<__main__.Person object at 0x104de83a0(=>this is memory address for this object)> thats mean this Person object at this location __main__ is running at main file that you're running this program.

# print(type(p1)) # <class '__main__.Person'>



# how to add function!!!!

# class Person: # fist char need to capital.
#     def __init__(self,name,age): 
#         self.name = name # inside of this,it will create attribute. an attribute is data associated with an instance.(インスタントに関連付けられたデータのこと)
#         # all self will access to an sttribute
#         self.age = age
        
# p1 = Person("Sayo",28) 
# p2 = Person("Kai",30)  
# print(p1.name,p1.age) # Sayo 28
# print(p2.name,p2.age) # Kai 30


class Fruit:
    def __init__(self,name,calorie):
        self.name = name
        self.calorie = calorie

apple = Fruit("apple",90)
apple.color = "red" # we can add new info for specific 
grapes = Fruit("grapes",120)

print(apple.name,apple.calorie)
print(grapes.name,grapes.calorie)









