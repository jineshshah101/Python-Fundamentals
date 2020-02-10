# This is a simple list

list = [1, 2, 3]
print(list)

# complicated list that holds multiple data types including list within a list

second_list = [2, "Katakuri", "Slam Jam", 3.4, False, [1,2,3] ]
print(second_list)

# can index lists where we can print a certain element in the list

print(second_list[0])
print(second_list[1])
print(second_list[2])
print(second_list[3])
print(second_list[4])
print(second_list[5])

# a list of names

names = ["Roger", "Whitebeard", "Garp"]
print(names)

# going to append another name to the list, ie add another name to the end of a list

names.append("Sengoku")
print(names)

# going to use an insert, ie lets you put another name in what position you want to put it at
# could be at the beginning or middle or end, got to specify it in the parameter

names.insert(0,"Rocks")
print(names)
names.insert(2, "Shiki")
print(names)

# use remove to remove an element from a list
# it's case sensitive

names.remove("Garp")
print(names)

# use reverse to reverse the order of a list

names.reverse()
print(names)

# use a sort to sort numbers in a list
# will automatically be in ascending order
# use reverse will bring the numbers in the list to descending order

unsorted_numbers = [3,2,5,1,9]
print(unsorted_numbers)
unsorted_numbers.sort()
print(unsorted_numbers)
unsorted_numbers.reverse()
print(unsorted_numbers)

# you can iterate over a list so each element of a list can do something depending on what you want it to do

for numb in unsorted_numbers:
    print(numb)