# filehandling
# Read a file
file = open ("ab.txt","r") #  first open a file to read the file 
data = file.read() # new variabl to read the data 
print(data) # then print 
file.close() # close at last

# write a file
file = open ("ab.txt","w") # open file
file.write("my name is python") # and write whatecer data you want 

file.close()
# write mulitple data
file = open("ab.txt", "w") # first we have to open file 
file.write("name:komal" ) #second write 
file.write("\ncourse:python") #second write 
file.close()

# append data in existing file
file = open("ab.txt","a") # first we have to open file 
file.write("\nname:Panda") #second write 
file.close() # then close 

# alias (short name )
with open ("ab.txt","r") as f:
    f.read()
    print ("----",f)

# csv = , seperate value   
import csv 
with open ("student.csv","w",newline = "" ) as file:
    writer = csv.writer(file) #creating csv file
    writer.writerow(["name","course","marks"]) # insert values 
    writer.writerow(["Komal","python",35])
    writer.writerow(["khushi","java",30])
    
# read CSV file
with open ("student.csv", "r") as file:
    reader = csv.reader(file) #reader read the file 
    for row in reader:
        print (row)

# JSON file
import json 
teacher = {"name": "shivani" ,"course": "python" } # creating student json with json format w
with open ("teacher.json","w") as file :
    json.dump(teacher,file, indent=17) # indent use for left space  dump Writes a file.
# read json file
with open ("teacher.json", "r") as file :
    data =json.load(file) # load reading from a file 
    print(data["name"])
    print(data["course"])
  
