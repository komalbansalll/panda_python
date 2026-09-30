# only print 4 times
a = ["apple","banana","mango","grapes","orange"]
print(a[0:4])
# now add one more element at the end of the list onl;y used for list method
a.append("pineapple")
print("append --",a)

#  clear method remove all the element from the list
a.clear()
print(a)

#  copy method
X = [10,20,30,40,20]
y = X.copy()
print("copy --",y)

# cout retiuen the number of elemet from the pecific valuse

a = X.count(20)
print("count --",a)

# extend all the elemt odf the list to the end of the current list 
a=["pink","blue","green"]
b=["car","bicycle","motorcycle"]
a.extend(b)
print("extend --",a)

# index return the index of the first element with the specific value
z = a.index("blue")
print("index value --",z)

# pop method remove the element in specific position
a.pop(1)
print("pop --",a)

# remove the first value from the speafic value 
a.remove("green")
print("remove --",a)

# reverse the order of the list
a=["pink","blue","green"] 
a.reverse()
print("reverse --",a)

# sort 
b =["a","c","d","b"]
b.sort()
print("sort --",b)