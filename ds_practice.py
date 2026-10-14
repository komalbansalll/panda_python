# Create a string and print its first and last characters
string = "Komal"
print(string[0:4])

# Convert the string "python programming" to uppercase.
string = "python programming"
print(string.upper())

# Create a list of five numbers and print the largest and smallest.
numbers = [10,20,55,76,100]
 
print(max(numbers))
print( min(numbers))

# Add an item to a list, remove an item and sort the list.
item = [1,5,4,7,8,9,3,10]
item.remove(5)
item.append(90)
print(item)
print(sorted(item))

# use list comprehension to create squares from 1 to 10.


# Create a tuple of three cities and print the second city.
cities = ("Paris", "London", "Tokyo")
print(cities[1])

# Create a set from [1, 2, 2, 3, 3, 4] and print the unique values.
numbers = [1, 2, 2, 3, 3, 4]
unique_values = set(numbers)

print(unique_values)

# Find the union and intersection of two sets.
a = {1,2,3}
b = {3,4,5}
print(a|b) # union 
print( a & b) # intersection 

# Create a student dictionary with name, age and course.
student = {
    "name": "koko",
    "age": 20,
    "course": "Computer Science"
}

print(student)

# Loop through a dictionary and print each key and value.

