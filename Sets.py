# Sets are represented as {}
# can add and take out things from sets
# no duplicates
# will be printed in random order no sequence

PiratesCrews = {"StrawHat", "Whitebeard"}
print(PiratesCrews)

# adding elements into the set
# note if you add the same element that is already in the set it won't be added since it doesn't do duplicates

PiratesCrews.add("RedHair")
print(PiratesCrews)

# having a list with duplicates
# you can cast it into a set to remove the duplicates
# then cast that result back to the list to get rid of duplicates to the list

h = [1,2,3,3,4,4,4,5]
print(h)
no_duplicate_set = set(h)
print(no_duplicate_set)
no_duplicate_list = list(no_duplicate_set)

# will replace the original list

h = no_duplicate_list
print(h)

# Look at a venn diagram to understand this example better

Monster = {"Luffy", "Zoro", "Sanji", "Jimbei"}
Medium = {"Jimbei", "Franky", "Robin", "Brook"}

# If we do a union of 2 sets just like in the venn diagram it will have all the elements of both sets and no repeats
# In this case there won't be 2 jimbei's

StrawHats = Medium.union(Monster)
print(StrawHats)

# If we do the intersection of 2 sets just like in the venn diagram there should only show elements that are the same
# in both sets in that intersection
# In this case it will just print out Jimbei

SameStrawHats = Medium.intersection(Monster)
print(SameStrawHats)

# If we do the difference of 2 sets it will tells us what isn't the same between the 2 sets
# In this case we want to know how is the medium set different from the monster set
# it will print out all the different elements in the Medium set

DiffStrawHats1 = Medium.difference(Monster)
print(DiffStrawHats1)

# If we switch it arround wanting to know the difference between the 2 sets
# it will print out all the different elements in the Monster set

DiffStrawHats2 = Monster.difference(Medium)
print(DiffStrawHats2)

# using the clear function allows you to clear out an entire set

ClearStrawHats = StrawHats.clear()
print(ClearStrawHats)