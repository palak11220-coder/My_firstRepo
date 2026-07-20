info = {'name' : "Karan", 'age':19, 'eligible': True}
print(info)
#Dictionary are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
#Accessing Dictionary items: Values in a dictionary can be accessed using keys. We can access dictionary value by mentioning keys either in square brackets or by using get method.
#print(info.get('name')) or print(info['name']) are same but different is that 
#print(info.get('name2')): it prints none and print(info['name2']): shows error

#for accessing multiple values we use
print(info.keys())

for key in info.keys():
    print(info[key])

#print(info.items()): it prints key-value pairs.
    
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value} ")    