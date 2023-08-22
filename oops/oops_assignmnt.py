"""
Assignment – Oops

1. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use _init_ method to construct some parameters

2. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
(Just try )

Hints:
Consider use yield

3. Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in _init_ method
    You can init a object with construct parameter or set the value later

4. Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.

5. Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.

6. Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.

7. Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.

8. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.

9. Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.
"""








"""1. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use _init_ method to construct some parameters"""

#
# class string:
#     def __init__(self,name):
#         self.name=name
#
#     def getstring(self):
#         print("string is:", self.name)
#
#     def printstring(self):
#         print(self.name.upper())
#
#     def test(self):
#         print("hello",self.name)
#
#
#
# name=input("enter a name:")
# obj=string(name)
# obj.getstring()
# obj.printstring()
# obj.test()


"""
2. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
(Just try )

Hints:
Consider use yield
"""
# class gen:
#     def __init__(self,num):
#         self.num=num
#
#     def number(self):
#         for i in range(1,self.num+1):
#             if i%7==0:
#                 print(i,end=" ")
#
# num=int(input("enter a range:"))
# obj=gen(num)
# obj.number()

"""
3. Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in _init_ method
    You can init a object with construct parameter or set the value later
"""
# class Myclass:
#     class_param="class parameter"
#     def __init__(self,inst_param=None):
#         self.instant_parameter=inst_param
#
# obj=Myclass()
# obj1=Myclass("instant parameter")
#
# print(obj.class_param)
# print(obj.instant_parameter)
#
# print(obj1.class_param)
# print(obj1.instant_parameter)

"""
4. Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.
"""
# class American():
#     def name(self):
#         def print_nationality():
#             print()
#         return print_nationality()

"""
5. Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.
"""
# class American:
#     def america(self,natioality):
#         self.nation=natioality
#
# class Newyorker(American):
#     def __init__(self):
#         super().america("american")
#         print(self.nation)
#
#
# obj1=Newyorker()
# obj1.nation

"""6. Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method."""
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def getRadius(self):
#         print("radius: ",self.radius)
#
#     def getArea(self):
#         print("area:",math.pi*self.radius**2)
#
# obj=Circle(100)
# obj.getRadius()
# obj.getArea()

"""
7. Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
"""
# class Rectangle:
#     def __init__(self,length,bredth):
#         self.length=length
#         self.breadth=bredth
#
#     def para(self):
#         print(self.length,self.breadth)
#
#     def area(self):
#         print(self.length*self.breadth)
#
# obj=Rectangle(100,52)
# obj.para()
# obj.area()

"""8. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class."""

# class Shape:
#     def __init__(self,area):
#         self.area=area
#
#
#     def area(self):
#         print("area of ",self.area)
#
# class Squre(Shape):
#     def __init__(self,length):
#         super().__init__(self.area)
#         self.length=length
#
#     def area(self):
#         print(self.length*self.length)
#
# obj=Squre(4)
# obj.area()

"""
9. Define a class Person and its two child classes: Male and Female. 
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.

"""
# class Person:
#     pass
#
# class Male(Person):
#     def getgender(self):
#         print("male")
#
# class Female(Person):
#     def getgender(self):
#         print("female")
#
# obj=Male()
# obj1=Female()
# obj.getgender()
# obj1.getgender()

"""----------------------------------------------"""
# class Staff:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary
#
#     def show_detail(self):
#         print("name:",self.name)
#         print("age :",self.age)
#         print("role:",self.role)
#         print("department:",self.dept)
#
# class Teacher(Staff):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("teacher","science",2500)
#
# obj=Teacher("sagil",23)
# obj.show_detail()
# print(obj.__dict__)

"""-----------------------------------------------"""
# class Animal:
#     def __init__(self,identity,age):
#         self.identity=identity
#         self.age=age
#
#     def feature(self):
#         if self.age==10:
#             return True
#         else:
#             return False
#
# obj=Animal("lion",10)
# obj.feature()
# print(obj.__dict__)

"""---------------------------------"""
# class Animal:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#
#     def __str__(self):
#         return f"rectangle length= {self.length} and rectangle width= {self.width}"
#
# obj=Animal(5,10)
# print(obj.__str__())

"""---------------------------------------"""
# class Teacher:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.__salary=salary
#
#     def getinfo(self):
#         print(self.name)
#         print(self.age)
#         print(self.__salary)
#
#
# obj1=Teacher("sagil",23,25000)
# obj1.getinfo()
# print(obj1.name)
# print(obj1.__salary)  #error,we cant access private data
