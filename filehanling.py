# filehandling
# Read a file
file = open ("ab.txt","r")
data = file.read()
print(data)
file.close()

# write a file
file = open ("ab.txt","w")
file.write("my name is python")

file.close()
# write mulitple data
file = open("ab.txt", "w")
file.write("name:komal" )
file.write("\ncourse:python")
file.close()

# append data in existing file
file = open("ab.txt","a")
file.write("\nname:Panda")
file.close()

# alias (short name )
with open ("ab.txt","r") as f:
    f.read()
    print ("----",f)

# csv = , seperate value   
import csv 
with open ("student.csv","w",newline = "" ) as file:
    writer = csv.writer(file)
    writer.writerow(["name","course","marks"])
    writer.writerow(["Komal","python",35])
    writer.writerow(["khushi","java",30])
    
# read CSV file
with open ("student.csv", "r") as file:
    reader = csv.reader(file) 
    for row in reader:
        print (row)

# JSON file
import json 
teacher = {"name": "khushi" ,"course": "python" }
with open ("teacher.json","w") as file :
    json.dump(teacher,file,indent=4)
# read json file
with open ("teacher.json", "r") as file :
    data =json.load(file)
    print(data["name"])
    print(data["course"])
  
