# dictionary
# left of the : is the key and right of the : is pair

food = {"Pizza" : 3, "Pasta" : 5}

# you index into a dictionary not with the normal 0 to etc number
# it is index by typing in the the name of the key
# if you put in a keyname that isn't in the dictionary you get a key error

print(food["Pizza"])

# inside dictionaries you can put a list inside of it
# also have a dictionary inside a dictionary
# it helps to make things easier instead of making complicated lists

FutureKings = {"Ikki" : {"Road" : "Wing Road", "Title" : "Sky King", "Nickname" : "Crow"},
               "Kazu" : {"Road" : "Flame Road", "Title" : "Flame King", "Nickname" : "Stealth"},
               "Onigiri" : {"Road" : "Gaia Road", "Title" : "Gem King", "Nickname" : "Pig"},
               "Buccha" : {"Road" : "Over Road", "Title" : "Rumble King", "Nickname" : "Tank"},
               "Agito/Akito" : {"Road" : "Bloodyfang Road", "Title" : "Fang King", "Nickname" : "Shark"},
               "Simca" : {"Road" : "Aqua Road", "Title" : "Water Queen", "Nickname" : "Swallow"},
               "Ringo" : {"Road" : "Sonia Road", "Title" : "Thorn Queen", "Nickname" : "Crazy Apple"},
               "Nue" : {"Road" : "Rising Road", "Title" : "Thunder King", "Nickname" : "The Lord of Thunder"}
               }

print(FutureKings["Ikki"])
print(FutureKings["Kazu"]["Nickname"])

# using the item method for dictionary
# get a list of tuples based on the key value pairs
# must make sure to cast it as a list so the value will not have the dict word in it

FutureKingsItems = list(FutureKings.items())
print(FutureKingsItems)

# using the key method for dictionary
# get a list of the key values from the dictionary
# must make sure to cast it as a list

FutureKingsKey = list(FutureKings.keys())
print(FutureKingsKey)

# using the value method for dictionary
# get a list of the values from the dictionary
# must make sure to cast it as a list

FutureKingsValue = list(FutureKings.values())
print(FutureKingsValue)

# you can remove an item from the dictionary using the pop function

FutureKingPop = FutureKings.pop("Ikki")
print(FutureKingPop)

# you can also remove a random item from the dictionary using the popitem function

FutureKingPopRandom = FutureKings.popitem()
print(FutureKingPopRandom)

# you can add an item into a dictionary

food["Taco"] = 9
print(food)

# clear an entire dictionary

EmptyFutureKings = FutureKings.clear()
print(EmptyFutureKings)