# dictionaries are used tostore data values in "keys:value"
# dictionary e.g food
#attributes of a dictionary
print(dir(dict))
print(help(dict))
food = {"breakfast":"toast & eggs", "lunch":"rice & fish", "dinner":"ice cream sundae"}
print(food)
# access items
print(food.get("lunch"))
print(food.get("brunch"))# will return none
if food.get("breakfast"):
    print("yes, breakfast is served")
else:
    print("There is no breakfast")
#update items 
food.update({"brunch":"berries salad"})
print(food)
# to remove an item
print(food.pop("breakfast"))
print(food)
food.popitem()# removes lastitem
print(food)
#to clear a dictionary
food.clear()
print(food)
# to get all the keys in a dictio nary
food.keys() 
print (food.keys())
#using for loop to iterate
for key in food.keys():
    print (key)
#to get all the values i na dictio nary
food.values()
print(food.values())
# to iterate it
for value in food.values():
    print (value)
# to get all the item ina dictionary
food.items()#looks like a list of tuples
for keys, items, in food.items():
    print(f"{keys}:{items}")
    