# creatong class
class student: 
    def display(self):
        print("welcome")

# object 
s1 = student()       
s1.display()



# class with attributes and object
class student :
    name = "rahul"
    age = 21

#  creating obj to call class
s1 = student () #creates new object s1 is the variable that refers to that object.
print (s1.name)

s2 = student () #same class alwyas
s2.name = "priya"
s2.age = 22
print(s2.name)


# class is the Python keyword used to create a class.

# student is the class name.

# name = "rahul" is a class attribute.

# age = 21 is another class attribute.

# example
class car: #define a class name car
    brand='bmw' 
    color='purple'

car1=car()
print(car1.brand)
print(car1.color)

car2=car()
car.brand='tata'
car.color='black'
print(car2.brand)
print(car2.color)

car3=car()
car.brand="audi"
car.color="white"
print(car2.brand)
print(car2.color)

class fruit:
    a='apple'
    b='mango'

f1=fruit()
print(f1.a)
print(f1.b)

f2=fruit()
f2.a='cherry'
f2.b='banana'
print(f2.a)
print(f2.b)


#  __init__() constructor

class student:
    def __init__(self, name,age,city):
        self.name = name 
        self.age =age 
        self.city = city 
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("city:",self.city)

s1 = student("komal",22,"delhi")
s1.display()
  
# Instance Method works with the data of a particular object
class student:
    def display(self): #instance self refer to the current object
        print("hello")
s1 = student()   
s1.display()


class student:
    def display(self):
        print(self.name)
s1 = student()
s1.name = "komal"
s1.display() 

# Class Method works with class level dta uses @classmethod

class student:
    school  = "PIT" #difine class var

    @classmethod # coverts the method into class method
    def display(cls): #cls define class
        print(cls.school) # print class var school

student.display() 

# changing class level data

class student :
    school='pit'
    @classmethod
    
    def change_school(cls,new_school):
        cls.school=new_school

student.change_school('dps') 
print(student.school)

# decorator.  method

def my_decorator(func):
    def wrapper():
        print('before function')
        func()
        print('after function')
    return wrapper

@my_decorator
def hello():
    print('b')
hello()

# static method @staticmethod 
class cal :
    @staticmethod
    def add(a,b):
        print("staticmethod",a+b)

cal.add(10,10)