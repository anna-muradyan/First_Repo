#! /usr/local/bin/python
# a = Fruit()
# b = Fruit()
# c = Fruit()
# a.name = "apple"
# a.weight = 120
# a.size = 25



# b.name = "orange"
# b.weight = "150"
# b.size = 30

# c.name = "limon"
# c.weight = 160
# c.size = 40

# print(a.name, a.weight, a.size)
# print(b.name, b.weight, b.size)
# print(c.name, c.weight, c.size)

class Greeter:
    def hello_world(self):
        print("hello world")
    
    def greeting(self, name):
        print("Hello,{}:".format(name))

    def start_talking(self, name, weather_is_good):
        print("hello,{}:".format(name))
        if  weather_is_good:
            print("today is a good weather, isnt it?")
        else: 
            print("Today is terrible")

greet = Greeter()
greet.hello_world()
greet.greeting("Peto")
greet.start_talking("Sasha", False)

class Car:
  
    def __init__(self, color):
        self.engine_on = False  
        self.color = color
        
    def start_engine(self):
        self.engine_on = True

    def drive_to(self, town):
        if self.engine_on:
            print("{}: We are going to  town {}:".format(self.color,town))
        else:
            print("{}: Problem with the car:".format(self.color,town))

car1 = Car("Red")
car2 = Car("Green")
car1.start_engine()
car1.drive_to("Yerevan")
car2.drive_to("Losabon")
# car2 =  Car()
# car1.start_engine()
# car1.drive_to("Yerevan")
# #car2.start_engine()



