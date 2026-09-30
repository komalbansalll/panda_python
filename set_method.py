# # # SET METHOD 28 september

# numbers = {10,20,30,40}
# print("original set ",numbers)
# # add one item to the set
# numbers.add(50)
# print(numbers)
# # update used for add multiple items
# numbers.update([60,70])
# print(numbers)
# # remove item used to remove specofic item 
# numbers.remove(10)
# print(numbers)

# # # if desnt exist no error occurs
# numbers.discard(30)
# print("discard",numbers)

# # # pop remove the last item from the set
# item = numbers.pop()
# print("removed", item)
# print(numbers)

# # # clear used to remove all the items
# numbers.clear()
# print(numbers)



new_set = {10,20,30,40}
new_numers = new_set.copy()
print(new_numers)

a  = { 10 , 20 , 30 ,40}
b = { 30 , 40 , 50 ,60}
#  union used to combine to set remove dublicate value
print("union of two set",a.union(b))
print("union of two set",b.union(a))



# intersection used to find common items
print("intersection of two set",a.intersection(b))

# diffrence used to find iyems that are only in a variuable and not in b variable 
print("diffrence of two set",a.difference(b))
print("diffrence of two set",b.difference(a))

# symmetric diffrence used to find non common itmes from both the sets 
print("symmetric diffrence of two set",a.symmetric_difference(b))

# --------------------------------------------------------------
c = { 10 , 20, }
d = {10 , 20 , 30 ,40}

# check weather all items are present in c and d
print ("issubset",c.issubset(d))

#  is super set check weather all items are present in d conastins alll ites of  c
print ("issuperset",d.issuperset(c))

c = { 10 , 20, 30}
d = {30 ,40}


# check esther two set have no common items  if comman valuee then false otherwise true
print("isdisjoint",c.isdisjoint(d))

# add one item to the set
# update used for add multiple items
# remove item used to remove specofic item 
# if desnt exist no error occurs
# pop remove the last item from the set
# clear used to remove all the items