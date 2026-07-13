#Lists in Python
l=[1,1,2,2,4,3,5,6]
m=["Red","Blue","green"]
print(l)
print(m)
print(type(m))
#indexing in Python
print(m[0])
print(m[2])

#List Methods
#list.sort():This method sorts the lists in ascending order. The original list is updated.
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

#list.append: it adds the element at the last.
#list.reverse: it reverse the list.
#list.count: Returns the count of the number of iteems with the given value.``````
print(num.count(2))
newlist = colors.copy()
print(colors)
print(newlist)
#insert(): This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
colors = ["violet", "indigo", "blue"]
colors.insert(1, "green") 
print(colors)

#extend(): This mmethod adds an entire list or any other collection datatype (set, tuple,dictionary) to the existing list.
rainbow = ["green", "yellow", "orange","red"]
colors.extend(rainbow)
print(colors)
#Concating two lists: You can simply concatenate two lists to join two lists.
colors2= ["yellow", "orange","red"]
print(colors + colors2)