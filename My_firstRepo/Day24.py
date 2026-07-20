#Tuples: Tuples are ordered collection of data items. They store multiple items in a single variable.Tuple items are seperated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.
Tup=(1,2,2,3,5,6)
print(Tup)
#Indexing in tuple
print(Tup[0])
print(Tup[-1])
countries=("Spain","Italy","India","England","Germany")
temp=list(countries) #change the tuple into list
temp.append("Russia") #Add item at the last
temp.pop(3) #remove item
temp[2] = "Finland" #change item
countries = tuple(temp)
print(countries)

#index() method: this method returns the first occurences of the given element from the tuple
#tuple.index(element, start, end): slice the part and gives the indexing of the given element
res = Tup.index(3)
print("first occurences of 3 is", res)