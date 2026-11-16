import pandas as pd

data = {"pyhton": 89,"java": 95}
a = pd.Series(data)
print(a)
print(a["pyhton"])
print(a.iloc[1])  #index number
print(a.loc["java"])

# series opreartion
a = pd.Series([10,20,30,40])
print(a+5)
print(a*2)
print(a/2)
print(a-2)

marks = pd.Series([85,95,75,80],index = ["rahul","priya","amit","ravi"])
print("all marks:",marks)
print("total marks:", marks.sum())
print("average marks:", marks.mean())
print("Highest marks:",marks.max())
print("lowest marks:",marks.min())
print("Ravi Marks:",marks["ravi"])

# DataFrame 2D Array
data = {"name":["rahul","ravi","rohit","priya","nisha"],
        "age":[22,12,28,29,21],
        "marks":[90,98,67,54,39]}
df = pd.DataFrame(data)
print(df)
 # create Df with custom index
df = pd.DataFrame(data,index=["a","b","c","d","e"])
print (df)
# select a single column
print(df["marks"])
# select multiple column
print(df[["name","marks"]])
# select only ravi's data
print(df[df["name"]=="ravi"])
print(df[df["name"]=="priya"])
 # select row usiing LOC()
print(df.loc["b"])
print(df.iloc[0]) 
# add a new column
df["city"] =["delhi","noida","gurgao","chennai","banglore"]
print(df)
# add a new row
df.loc["f"] = ["neha",34 ,99,"chandigah"]
print(df)
# delete a column 
df.drop("age",axis=1,inplace=True)
print(df)
# delete a row
df.drop("b",axis=0,inplace=True)
print (df)

data = {
"Name": ["Rahul", "Priya", "Amit"],
"Age": [22, 25, 23],
"Marks": [85, 90, 75]
}
df = pd.DataFrame(data)
df.drop(1, axis=0, inplace=True)
print(df)
 
# Series = A one-dimensional list of data, 
# similar to a single column in a spreadsheet.
data = [10,20,30,40]
a = pd.Series(data)
print(a)
 
datas = [85,90,75]
a = pd.Series(datas,index=["a","b","c"])
print (a)
# create csries using dictnory
course = {"python":90,"java":85,"c++":95}
a = pd.Series(course)
print(a)
print(a["python"])