# class Person:
#     def __init__(self,name):
#         self.name = name
#         self.age = None
    
#     def say_hello(self):
#         print(f"Hello, {self.name}")

#     def set_age(self,age):
#         self.age = age

#     def get_age(self):
#         return self.age
        

# p1 = Person("Sayo")
# p2 = Person("Kai")

# if you set up just like ..
# p1.get_age() # and you will be ERROR because, there is not age number! so..you need to put self.age = None inside __init__!! then, you wont be ERROR because, if you did not put the age number, it will be None.
# RECOMEND to put all attributes inside of initialization!!!!



# p1.set_age(28)
# p1.say_hello() #Hello, Sayo
# p2.say_hello() #Hello, Kai

# print(p1.age) # 28
# print(p1.get_age()) # 28

class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False
    
    def toggle_lock(self):
        # this is like.. if self.locked == True, self.locked = False else: ..
        self.locked = not self.locked

    def increment(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count += 1

    def decrement(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count -= 1

    def print_count(self):
        print(f"The current counr is {self.count}")

counter = Counter()
counter2 = Counter()

counter.toggle_lock()
counter2.increment()

counter.print_count()
counter2.print_count()




















