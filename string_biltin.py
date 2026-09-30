# capitalize first letter of the string
bxt="my name is komal"
# print("string. :",bxt)
x=bxt.capitalize()
print("capitalize :",x)

# casefold small first letter of the string 
bxt="My Name Is Komal"
print("string. :",bxt)
x=bxt.casefold()
print("casefold :",x)

# center method return the center of the string
bxt="komal"
# print(bxt)
x=bxt.center(100)
print("center :",x)

# count return the number of times the specific value is present in the string
bxt="my\tname\tis\tkomal"
# print(bxt)
x= bxt.count("is")
print("count :",x)

# expandtabs method used to set the tab size
y = bxt.expandtabs(15)
print("expandtabs :",y)

# lower method return the string in lower case
bxt="MY NAME IS KOMAL"
# print(bxt)
x=bxt.lower()
print("lower :",x)

# upper method return the string in upper case
bxt="my name is komal"
# print(bxt)
x=bxt.upper()
print("upper :",x)