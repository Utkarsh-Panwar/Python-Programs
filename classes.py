# -*- coding: utf-8 -*-

# class MyClass:
#  	"This is my first class"
#  	a = 10
#  	def func(self):
#          print('Hello')

# # Output: 10
# print(MyClass.a)

# # # Output: <function MyClass.func at 0x0000000003079BF8>
# print(MyClass.func)
# #MyClass.func()
# #
# ## Output: 'This is my second class'
# print(MyClass.__doc__)



#class MyClass:
#	"This is my second class"
#	a = 10
#	def func(self):
#		print('Hello')
#
## create a new MyClass
#ob = MyClass()
#
## Output: <function MyClass.func at 0x000000000335B0D0>
#print(MyClass.func)
#
## Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
#print(ob.func)
#
## Calling function func()
## Output: Hello
#ob.func()
#print(ob.func())




# class CoffeeMachine:
#     name = ""
#     beans = 0
#     water = 0

#     # def init_var(self, namee, beanse, watere):
#     #       self.name = namee
#     #       self.beans = beanse
#     #       self.water = watere
    
#     # def __init__(self):
#     #     self.name = "BlackBean"
#     #     self.beans = 78
#     #     self.water = 90
        
#     def __init__(self, name, beans, water):
#         self.name = name
#         self.beans = beans
#         self.water = water

#     def addBean(self):
#         self.beans = self.beans + 1

#     def removeBean(self):
#         self.beans = self.beans - 1

#     def addWater(self):
#         self.water = self.water + 1

#     def removeWater(self):
#         self.water = self.water - 5

#     def printState(self):
#         print("Name  = " + self.name)
#         print("Beans = " ,self.beans)
#         print("Water = " + str(self.water))

# #pythonBean = CoffeeMachine() 
# #pythonBean.init_var("Python Bean", 83, 20)
# pythonBean = CoffeeMachine("Python Bean", 83, 20)
# pythonBean.printState()
# print("")
# pythonBean.addBean()
# pythonBean.removeWater()
# pythonBean.printState()



#-----------------------Inheritance in Python------------------------------------------------
#class User:
#    name = None
#    job = None
# 
#    def __init__(self, name, job):
#        self.name = name
#        self.job = job

# 
#    def printName(self):
#        print("Name = " + self.name)
# 
#    def printJob(self):
#        print("Job = " + self.job)
# 
#class Programmer(User):
# 
#    language = ""
# 
#    def setLanguage(self, language):
#        self.language = language
# 
#    def printLanguage(self):
#        print("Language = " + self.language)
# 
#guido = Programmer("Guido","Developer")
#guido.setLanguage("Python")
#guido.printName()
#guido.printLanguage()
#guido.printJob()


'''
class Person:     
    name = ""  
    age = 0    
   
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
  
   
class Student(Person):
    studentId = ""  
  
    def __init__(self, studentName, studentAge, studentId):  
        Person.__init__(self, studentName, studentAge) 
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId  
  
  
person1 = Person("Richard", 23)  
person1.showAge()  

student1 = Student("Max", 22, "102")  
print(student1.getId())  
student1.showName() 
'''

'''
#Multiple Inheritance------------------------------------ 
class Person: 
    
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
  
   
class Student:
    def __init__(self, studentId):  
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId  
  
  
class Resident(Person, Student): 
    def __init__(self, name, age, id):  
        Person.__init__(self, name, age)  
        Student.__init__(self, id)  
  
  

resident1 = Resident('John', 30, '102')  
resident1.showName() 
resident1.showAge() 
print(resident1.getId())  
'''


#Multilevel Inheritance---------------------------------------------------------
class Animal:   
    def eat(self):  
      print('Eating...'  )
class Dog(Animal):  
    def bark(self):  
      print('Barking...'  )
class BabyDog(Dog):  
    def weep(self):  
        print( 'Weeping...'  )
d=BabyDog()  
d.eat()  
d.bark()  
d.weep()  



#------------------Overridden method in python----------------------------------------
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
               
#     def getArea(self):
#     		print( self.length*self.breadth," is area of rectangle")
# class Square(Rectangle):
#     def __init__(self,side):
#         self.side = side
#         Rectangle.__init__(self,side,side)
#     def getArea(self):
#     		print( self.side*self.side," is area of square")
# s = Square(4)
# r = Rectangle(2,4)
# s.getArea()
# r.getArea()
