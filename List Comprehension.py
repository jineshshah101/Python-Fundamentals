# putting a list into a new list

icecreamtrio = ["Roxas", "Xion", "Axel"]

l = []
for trio in icecreamtrio:
    l.append(trio)
print(l)

# basic list comprehension

print([trio for trio in icecreamtrio])

# putting another list to append to another list but also adding a string as well

pasttrio = ["Terra", "Ventus", "Aqua"]

k = []
for ttrio in pasttrio:
    k.append(ttrio + " Not Favorite")
print(k)

# same thing achieved as above except with list comprehension

print([ttrio + " Not Favorite" for ttrio in pasttrio])

# making dictionary and putting it in a list with an if statement

destinytrioranking = {"Sora" : 8, "Riku" : 10, "Kairi" : 3}

n = []
for destinytrio in destinytrioranking:
    if destinytrioranking[destinytrio] > 6:
        n.append(destinytrio)
print(n)

# same thing achieved as aboved except with list comprehension

print([destinytrio for destinytrio in destinytrioranking if destinytrioranking[destinytrio] > 6])
