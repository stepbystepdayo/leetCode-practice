
# class Person: # we need to put class sigler name! not pural. 
#     def __init__(self, name):
#         self.name = name
#         self._salary = 0
    
#     # we can not accesse salary outside of class so, if you want to modify it, make new class
    
#     def set_salary(self,salary):
#         if salary < 0:
#             raise ValueError("Hey, This is invalid!")
#         self._salary = salary
    
#     def get_salary(self):
#         return round(self._salary)
    
'''
    salary = property(get_salary,set_salary)
    # propertyを使うことによって、複数のクラスを実行させ最終的な答えを出すことができる。この場合、get_salaryとset_salaryを同時に出せる。

    
'''

class Person: 

    def __init__(self, name):
        self.name = name
        self._salary = 0

    '''
    @property 
    違う方法でのpropertyを作る方法は、クラスの前に@propertyを使うこと。同時に動作させたい他のクラスの前には@同じクラス名.setterでクラスは同じ名前にすること。
    q
    '''
    @property 
    def salary(self):
        return round(self._salary)
    
    @salary.setter
    def salary(self,salary):
        if salary < 0:
            raise ValueError("Hey, This is invalid!")
        self._salary = salary
    

p = Person("Sayo")
p.salary = 10.222
print(p.salary) # 10


'''
# PRIVATE ATTRIBUTE:
if you do NOT want to change salary value and you want to tell someone DO NOT CHANGE salary attribute, put underscore _ before salary => self._salary: this is Private attribute. this is like a notion to someone Don't use this system. 



# PUBLIC ATTRIBUTE:
On the other hands, public attribute is accessible from anywhere outside the class.

'''

class Time:
    def __init__(self, second):
        self._second = second
    
    @property
    def second(self):
        return self._second

    @second.setter
    def second(self,second):
        if second < 0 or second > 60:
            raise ValueError("Invalid!")
        self._second = second

t = Time(50)
t.second = 59
print(t.second)

'''
if the attribute has a specific base value, you need to use private attribute and you have to set up to someone can not modify this value from the outside of class. but if you want to change the value, use the property and return new value.
'''

'''
getter and setter 
クラスを分けるとき、情報を得る｜その情報を何かに設定する　という過程を分けた方がわかりやすくなる

'''