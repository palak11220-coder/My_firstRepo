#sets method
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2)) #s1 and s2 keep untouched while using this method
s1.update(s2) #s1 value change after this method
print(s1.intersection(s2))
s1.intersection_update(s2)

#symmetric difference: (A-B)u(B-A)or(AuB)-(AnB)
s3 = s1.symmetric_difference(s2)
print(s3)
#difference 
s3 = s1.difference(s2)
print(s3)
#isdijoint(): checks if items of the given sets are present in another set, returns false if items are present,else it returns false.
#issuperset(): checks if all the items of a particular set are present in the original set. it returns true if all the items are present, else it returns false.
#issubset(): checks if all the items of the original set are present in the particular set.It returns true if all the items are present, else it returns False
#add(): to add a single items in the set use the add() method. 
#update(): to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
#remove()/discard(): to remove items from the list.
#pop(): This method removes the last item of the set but the catch is that we dont know which items gets popped items if you assign the pop() method to a variable.
#del: del is not a method, rather it is a keyword which deletes the set entirely.
# clear(): This method clears all the items in the set and prints an empty set.
