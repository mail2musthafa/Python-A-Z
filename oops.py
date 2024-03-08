#this session we will cover the oops concepts in python 
#class is blue print or template or model or disign or  plan
#object --a physical existance or  instance of a class 
# reference variable :refernce variableis refers to perform required operation on objcect
#perobject an number of variable may be there 
# if refernce vriable is not prsent of any object then we cont use the object for  dffernet operation the no use of creation object 
# class---<object<---refernce variable 
#class 
    # properties or attributes or Variables 
    # behaviour  by using methods 
    # methods --actions 

# class className:
    #'''Documentation string represets descrotion of object'''
    # variables==properties or attributes
    # methods or attribies or Behaviours

class Student:
    '''this sample demo while cration class '''
    #variables 
    #methods 
Student()  
print(Student.__doc__)
help(Student)
#Withi in the pytho  class there typs of variable 
# variable(3)
# instant variable   --object level variable 
# static varaible ---class level variable 
# local variable  --methods level vaiable

# metods(3)
# instant methods 
# class methods
# static methods 
class Student:
    '''class devlaped for demo '''
    def __init__(self):
        self.name = 'md' 
        self.rollnumber = 100
        self.marks = 99
    def talk(self):
        print('hello i am ',self.name)
        print('my marks are ',self.marks)  
object = Student()
print(object.name) 
print(object.marks)     
print(object.rollnumber)
object.talk()
#---------------------------------------------
class Student:
    def __init__(self,name,rollnum,marks):
        self.nmae = name
        self.rollnum = rollnum
        self.marks = marks
    def chat(self):
        print('my name is :',self.name)
        print('my rollnumber is :'self.rollnum)
        print('my marks are :',self.marks)
object1 = Student('md',100,80)
object1.chat()
#------------------------------------------------
class Dog:
    #class attributes 
    attr1 = 'mammal'
    #Instance attribite
    def __init__(self,name):
        self.name = name
#object instantiation 
german_shappord = Dog('German Shappord')   
print(german_shappord.name)
print(tommy.name)
#print() 
#-------------------------------------
class Dog:
 
    # class attribute
    attr1 = "mammal"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
 
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
#----------------------------------------------------
'''creating the class and objects with methds'''
class Dog:
    #class attribute 
    attr1= 'mammal'
    #instatace attrubutes
    def __init__(self,name):
        self.name = name
    def speak(self):
        print('my name is {}'.format(self.name))
Rodger = Dog('Rodger')  
Tommy = Dog('Tommy')     
print(Tommy)
print(Tommy.name)
#------------------------------------------------
 
# parent class
class Person(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
     
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
 
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using
# its instance
a.display()
a.details()
#self and constructer  
# self is refernce variabe  which is always pointing to current object 

class Test:
    def __init__(self):
        print('address of object pointed by self',id(self))

t = Test()    
print(t)
print('addres of object pointed by t',id(t))
#--------------------------------
class Test:
    def __init__(self):
        print('constructer ')
    def m1(self,x):
        print('x value ',x)    
t  = Test()     
t.m1(10)   


#369380139351  
 ####################################################################   

# In python,object-orirented  programming(OOPS)is a programming paradigm 
# that uses objects and clasess in programming,it aims to implement real -world entities like inheritence 
# polmorphisms,encapsualtion etc 
#Class
# Obejects
# Polymophism
# encapasualtion 
#inheritance 
# Data Abstraction 

class Dog:
    print('welcome dog object created successfully')
# creating Dog class object
dog_object =Dog()
print(dog_object)
#---------------------------------------
class Dog():
    #class level attributes 
    attr1 = "mammal"
    #instance attribute
    def __int__(self,name):
        self.name = name

#object instantiation        
Rodger = Dog('Rodger')
Tommy  = Dog('Tommy') 
#accessing the class level attributes 
print('rodger is a {}'.format(Rodger.__class__.attr1))

class Dog:
 
    # class attribute
    attr1 = "mammal"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
 
# Driver codedfghjkl;
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))



    
 



          

     


