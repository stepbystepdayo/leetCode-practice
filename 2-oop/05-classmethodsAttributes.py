
'''
class mathod can not access anthing related instance.
just related to the class
'''


class Car:
    number_of_cars = 0
    wheels = 4
    def __init__(self,make,model):
        self.make = make
        self.model = model
        Car.number_of_cars += 1
    
    @classmethod
    def update_number_of_cars(cls,cars):
        cls.number_of_cars = cars
        print("run")
        

c1 =Car("Ford","Edge")
c1 =Car("Tesla","Model3")

Car.number_of_cars += 3

print(Car.number_of_cars)

class Circle:
    pi = 3.14

    @classmethod
    def area(cls,radius):
        return cls.pi * (radius * 2)

    @classmethod
    def perimeter(cls,radius):
        return 2 * cls.pi * radius
    

    @classmethod
    def get_area_and_perimeter(cls,radius):
        return cls.area(radius), cls.perimeter(radius)

print(Circle.get_area_and_perimeter(4))