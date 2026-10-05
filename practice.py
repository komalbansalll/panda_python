# # # addition operator
# # # Write a program to add two numbers. 
# # a = 10 
# # b = 10
# # print ("addition operator :", a + b)

# # # substraction operator
# # # Write a program to subtract two numbers.
# # a = 10 
# # b = 10
# # print ( "substraction operator :", a - b)

# # # multiplication operator
# # # Write a program to multiply two numbers.
# # a = 10 
# # b = 10
# # print ("multiplication operator :",a * b)

# # # division operator
# # # Write a program to divide two numbers. 
# # a = 10 
# # b = 10
# # print ("division operator :",a / b)

# # # mod operator

# # a = 10 
# # b = 10
# # print ("mod operator :",a % b)

# # # comparsion operator
# # # Write a program to check whether two numbers are equal or not.
# # a = 10 
# # b = 10
# # print ("comparsion operator :",a == b)

# # a = 10 
# # b = 10
# # print ("comparsion operator :",a != b)  

# # # Write a program to check if a number is greater than another number. 
# # a = 10 
# # b = 10
# # print ("comparsion operator :",a > b)

# # #  or & and 

# # a = 10 
# # b = 10
# # print ("logical operator :",a > b or a < b)

# # a = 10 
# # b = 10
# # print ("logical operator :",a > b and a < b)

# # #  identy operator
# # a = 100
# # b = 10
# # print ("identy operator :",a is b)

# # a = 10 
# # b = 20
# # print ("identy operator :",a is not b)

# # # membership operator
# # # Write a program to check if a value exists in a list. 
# # a = ["komal","bansal"]
# # print("komal in a : ","komal" in a)

# # # Write a program to check if a value does not exist in a list. 
# # a = ["laptop"," mouse","keyboard"]
# # print("laptopfff not in a : ","laptopffff"  not in a)




# # # Write a program to check whether two variables refer to the same object.
# # a = ["car","bicycle","motorcycle"]
# # b = ["car","bicycle","motorcycle"]
# # print( "a id :", id(a))
# # print( "b id :", id(b))
# # c = a
# # print(id(c))
# # c = b
# # # print(c)
# # print ("c is b : ",c is b)
# # print ("c is a " , c is a )




# # x = ["apple", "banana"]
# # y = ["apple", "banana"]
# # z = x

# # print(x is z)

# # # returns True because z is the same object as x

# # print(x is y)

# # # returns False because x is not the same object as y, even if they have the same content

# # print(x == y)

# # # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# # x = ["apple", "banana"]
# # y = ["apple", "banana"]
# # z = x

# # print(x is not z)

# # # returns False because z is the same object as x

# # print(x is not y)

# # # returns True because x is not the same object as y, even if they have the same content

# # print(x != y)

# # # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# # # Check Positive or Negative 
# # num = int(input("Enter a number: "))
# # if num > 0:
# #     print("Positive")
# # elif num < 0:
# #     print("Negative")
# # else:
# #     print("Zero")

# #  #Take a number from the user and check whether it is even or odd.
# # num = int(input("Enter a number: "))
# # if num % 2 == 0:
# #     print("Even")
# # else:
# #     print("Odd") 

# # # Eligible to Vote
# # age = int (input("enter your age:"))
# # if age >=18:
# #     print("your are elegible for voting")
# # else:
# #     print("you are not elegible for voting")
    
# # # Find Greater Number
# # num1 = int(input("enter yor number :"))
# # num2 = int (input("enter your 2nd number :"))
# # if num1>num2:
# #     print("num1 is grester")
# # elif num1==num2:
# #     print("num1 and num2 are equal")
# # else:
# #     print("num2 is greater")
    
# # # Grade Calculator Take marks as input: 
# # # 90–100 → A+ 
# # # 75–89 → A 
# # # 60–74 → B 
# # # 40–59 → C 
# # # Below 40 → Fail 

# # marks = int(input("enter your marks :"))
# # if marks >=90:
# #     print("grade A+")
# # elif marks >=75:
# #     print("grade A")
# # elif marks >=60:
# #      print("grade B")
# # elif marks >=40:
# #     print("grade C")
# # else:
# #     print("fail")

# # # loop
# # # Print 1 to 10

# # for i in range (1,11):
# #     print(i)

# # # Print Even Numbers

# # for i in range (1,11):
# #     if i % 2 == 0:
# #         print(i)
        
# # # Print odd numbers
# # for i in range (1,11):
# #     if i % 2 != 0:
# #         print(i)

# # # Take a number from the user and print its multiplication table from 1 to 10

# # # num = int(input("enter your number :"))
# # for i in range (1,11):
# #     print(num,"*",i,"=",num*i)        

# # # Use a for loop to calculate the sum of numbers from 1 to 100. 

# # sum = 0
# # for i in range (1,100):
# #     sum = sum + i
# # print("sum----" , sum)


# # # Print numbers from 1 to 10, but stop the loop when the number becomes 5. 

# # for i in range (1,11):
# #     if i == 5:
# #         break
# #     print("break when 5 ----",i)


# # # Ask the user to enter numbers repeatedly. Stop the loop when the user enters 0. 

# # while True:
# #     num = int(input("enter your number :"))
# #     if num == 0:
# #         break
    
# # # Store a secret number, for example 7. Ask the user to enter a number repeatedly. 
# # # If the number is greater than 7 → print "Too High" 
# # # If the number is less than 7 → print "Too Low" 
# # # # If the number is 7 → print "Correct!" and stop the loop.

# # sec_num = 7
# # while True:
# #     num = int(input("enter your number :"))
# #     if num > sec_num:
# #         print("too high")
# #     elif num < sec_num:
# #         print("too low")
# #     else:
# #         print("correct")
# #         break


# # list builtin method 
# a = ["kiran","komal"]
# a.append("bansal")
# print (a)    


# 28 september practice 
# # 1. Create a set fruits = {"Apple", "Banana", "Mango"} and add "Orange" using add(). 
# fruits = {"apple","banana","mango"}
# fruits.add("orange")
# print("add  ",fruits)

# # 2. Create a set of numbers {10, 20, 30, 40} and add 50, 60, 70 using update(). 
# numbers= {10,20,30 , 30 , 30,40}
# numbers.update([50,60,70])
# print("after updating",numbers)

# # 3. Remove 30 from a set using remove(). 
# numbers.remove(30)
# print("after removing 30",numbers)

# # 4.  Try to remove 100 from a set using discard() without getting an error.
# numbers.discard(100)
# print("after removing 100 without getting error",numbers)

  
# # 5. Create a set and remove one item using pop(). Print the removed item. 
# a = { 10 ,20 , 30 ,40 ,100}
# b = a.pop()
# print ("pop=---",b)
# print(a)

# # Create a set and make a copy using copy(). 
# a = {10,20,10}
# b = a.copy()
# print(b)


# # Find the union of A and B.
# #  Using the same sets, find the common elements using intersection(). 
# set1 = {10,20,30}
# set2 = {30,40,50}
# print("intersection",set1.intersection(set2))

# # Find the elements that are present in A but not in B using difference(). 
# print("difference",set1.difference(set2))


# # Find the elements that are present in B but not in A. 
# print("symmetric difference",set1.symmetric_difference(set2))

# # Find all non-common elements using symmetric_difference(). 
# print("symmetric difference",set1.symmetric_difference(set2))

# #  Two students attended different courses:
# # Type to enter text 
# # python_students = {"Rahul", "Amit", "Priya", "Neha"}
# # java_students = {"Amit", "Neha", "Ravi", "Karan"}
# # Find:
# # Students enrolled in both courses 
# # Students enrolled only in Python 
# # Students enrolled only in Java 
# # Students enrolled in at least one course 
# # Students enrolled in exactly one course 


# python_students = {"Rahul", "Amit", "Priya", "Neha"}
# java_students = {"Amit", "Neha", "Ravi", "Karan"}

# print("enrolled in both courses",python_students.intersection(java_students))
# print("enrolled only in python",python_students.difference(java_students))
# print("enrolled only in java",java_students.difference(python_students))
# print("enrolled in at least one course",python_students.union(java_students))
# print("enrolled in exactly one course",python_students.symmetric_difference(java_students))


# 30 september funtions 

def greek():
    print("welcome to python ")
greek()
# 2. Name Function Create a function greet(name) that accepts a name and prints:Hello, Rahul
def greet(name):
    print("hello",name)
greet("rahul")

# 3. Addition Function Create a function add(a, b) that returns the sum of two numbers.
def add(a,b):
    return a + b
print("addition : ",add(3,4))

# 4. Subtraction Function Create a function subtract(a, b) that returns the difference of two numbers.
def sub(a,b):
    return a- b
print("subtraction :",sub(4,1))

# 5. Multiplication Function Create a function multiply(a, b) that returns the multiplication of two numbers.
def multi(a,b):
    return a*b
print("multiplication :",multi(2,8))
# 6. Division Function Create a function divide(a, b) that returns the division of two numbers.
def div(a,b):
    return a/b
print("division :",div(8,16))

# odd even


 
def check (a):
    if a % 2 == 0:
        print("even")
    else:
        print("odd")
# n = int(input("enter a numbe"))
# check(n)
 
# 8. Positive, Negative or Zero Create a function check_number(n) that checks whether a number is Positive, Negative, or Zero.
def check_number (n):
    if n==0:
        print("zero")
    elif n > 0 :
        print("positive")
    else:
        print("negative")
# n = int(input("enter your number : "))
# check_number(n)

# 9. Largest of Two Numbers Create a function largest(a, b) that returns the largest of two numbers.
def largest (a,b):
    if a>b:
        print("a is grater")
    else:
        print("b is grater")
a = int(input("enter your number : "))
b = int(input("enter your number : "))
largest(a,b)

# 10. Square of a Number Create a function square(n) that returns the square of a number.

def square(n):
    return n * n

num = int(input("Enter a number: "))
result = square(num)
print("Square:", result)

# 11. Cube of a Number Create a function cube(n) that returns the cube of a number.
def cube (n):
    return n * n * n
num = int(input("Enter a number: "))
result = cube(num)
print("Cube:", result)
# 12. Default Argument Create a function power(base, exp=2) using a default argument.
def power(base, exp=2): 
  return base**exp
print("default argument",power(3))
print("default argument",power(2,3))

# 13. Positional Arguments Create a function student(name, age) and call it using positional arguments.
def student(name, age):
    print("Name:", name)
    print("Age:", age)

# 14. Keyword Arguments Create a function student(name, age) and call it using keyword arguments:
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(name="John", age=25)    

# 15. *args Practice Create a function total(*numbers) that accepts any number of numbers and returns their total
def total(*numbers):
    return sum(numbers)
print("args",total(10,20,30,40))

# 16. **kwargs Practice Create a function student_info(**details) that accepts student information
def student_info(**details):
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Course:", details["course"])

student_info(name="John", age=25, course="Python")

# 17. Return Multiple Values Create a function calculate(a, b) that returns:
# Addition 
# Subtraction 
# Multiplication 
# Store the returned values in three variables.






# 18. Local Variable Create a function show() with a local variable x = 100. Print x inside the function and try to print it outside. Observe the error.

# 20. Mini Calculator Using Functions Create separate functions for:
# Addition 
# Subtraction 
# Multiplication 
# Division 
# Take two numbers from the user and display the results using these functions.

























