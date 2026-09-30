# LOOPS for , while , do while 

a = "komal"
# for i in a:
#     print(a)
for i in range(10):
    print (a)    

a = ["apple","banana","mango","grapes","orange"]
for i in a:
    print (i)

#  range start stop step
# for i in range (15,25):
#     print (i)

# for i in range(2,12,3):
#     print (i)

for i in range(1, 11 ):
    print ("2X", i ,"=", 2*i)

a = ["manvi","shivi","koko","aman"]    
for i in a :
    print (i)

# while loop
i = 1
while i <= 5:
    print(i)
    i = i + 1

i = 5 
while i>=1:
    print(i)
    i = i -1 

# while True :
#     num = int(input("enter yoyr number"))
#     if num == 5:
#         break
#     print("your enter number is :", num )

for i in range (1,11):
    if i ==9:
        break
    print(i)

for i in range (1,12):
    if i ==9:
        continue
    print(i)