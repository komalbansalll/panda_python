# data structure 
name = "komal"
msg = "hello"
print (name)
print(msg)

# indexing
word = "python"
print(word[0])
print(word[-1]) # return last value 

# string slicing 
word = "python" 
print(word[0:3]) # return pyt
print(word[1:4])
print(word[:4])
print(word[::-1]) # reverse the string 

text = "hello code"
print(text.strip())

text = "hello code"
print(text.startswith("hello"))
print(text.endswith("code"))

# string formatting
name = "komal"
age= 25
print(f'my name is {name} and my age is {age}')

# list indexing an slicing 
a = [10,20,30,40,50]
print(a[0])
print(a[1:3])
print(a[-1]) #print last value 
print(a[::-1]) #reverse

# nested list
students = [["komal",20],["shivai",19]]
print(students[1][0]) #a list that contains other lists as its elements.

# list comprehension
square = [ n*n for n in range (1,6) ]
print(square)

# tuple
color = ('red', 'pink' , "green","orange")
print(color[0])
print(color[1:3])

# tuple unpacking
stu = ("komal", 25 ,"delhi")
name , age , city = stu
print(name)
print(city)

# set operators
a = {1,2,3}
b = {3,4,5}
print(a|b) # union 
print( a & b) # intersection 
print(a-b) #difference
print (a^b) #symmetric diffrence

# nested dictonaries
student = {
    's1': {"name":"komal", "age " : 26},
    's2' : {"name":"shivani", "age": 19}

}
print(student["s2"]["age"])

# miutable can changed like set list , dict
# imutable can not be changed int, float, str, tuple, bool