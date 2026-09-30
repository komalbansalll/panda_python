# function 
def abc():
    print ("hello welcome to python")
name = "shree"    
if name == "komal":
 print("you are girl")
else:  
 print("you are boy")
 
 abc()

# function with parameter and argument 
# name is parameter and komal is argument
def kbc (name):
  
  print(name)
kbc("komal")

#  normal function syntax
def a():
  print("python")
a() 


# default argument
def b(name="komal"):
  print(name)
b()  

# return statement
def add(a,b):
  return a+b
 
result = add(40,20)
print(result)
# print(add(10,20))

def sub(a,b):
  return a-b
print(sub(10,20))
print(sub(a=4,b=10))

# default argument
def power(base, exp=2):
  return base**exp
print("default argument",power(3))
print("default argument",power(2,3))

# args store as a tuble in print 
def total(*numbers):
  return sum(numbers)
print("args",total(10,20,30,40))

# kwargs store as a dictionary in print
def info(**data):
#   for a,b are variables 
  for a,b in data.items():
   print(a, ":",b)
info(name="komal",age=20)

 
def info(**data):
#   for key , values are variables 
  for key,values in data.items():
   print(key, ":",values)
info(name="komal",age=20)

# returing multiple (values as tuble) 
def min_max(numbers):
  return min(numbers),max(numbers)
low,high = min_max([4,9,1,7])
print("loww",low,"high",high)



# scope variable
# local variable used inside the function and usable only there 
# global variable used inside and outside the function
 
x = 10 # global variable
 
def show():
  y = 5
  print(x+y)
show()
# print(y)  # show error because y is local variable

a = "my name is komal"
print(len(a)) # only use in string

b = [1,2,3,4,5]
print(max(b)) # only use in list