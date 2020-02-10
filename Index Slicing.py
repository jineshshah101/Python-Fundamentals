# a list of numbers
numbers = [0,1,2,3,4,5,6,7,8,9]

# printing out the first element of the list
print(numbers[0])

# can use negative indexing
# negative indexing goes in the opposite order of traveling through a list instead of going in the normal order

print(numbers[-1])

# we will be using ":" in the indexing
# : allows us to put a range of elements to access
# in this example it means including all elements up to the 3 index but not including the third index

print(numbers[:3])

# if you put a number before the : and a number at the end of the : you will specify the range much better
# This is called Slicing

print(numbers[0:8])

# you can also get substrings of strings using slicing as well

name = "Dogtooth Katakuri"
print(name[:6])

# slicing also works with negative indexing

print(numbers[0:-1])

# if you put an number in front of the : and nothing at the end for this slicing
# it will include that index value and will go all the way to the end of the list

print(numbers[4:])

# example of range with slicing

print(numbers[3:9])

# striding is something that has two ::
# the first : part will be the range but the second : part will mean how much you want to jump across the list
# in this example from the range we will jump across 1 element in the list in a sense skipping it

print(numbers[0:10:2])

# stride of 1 includes all elements no skipping
# stride of 2 will skip 1 element
# stride of 3 will skip 2 elements
# if you use negative indexs in strides that means you are skipping in the opposite direction

print(numbers[::1])
print(numbers[::2])
print(numbers[::3])
print(numbers[::-1])
print(numbers[::-2])
print(numbers[::-3])

# using slicing with variables
# requires a for loop
# range(len()) means taking the range from whatever the len of the list is
# in this example based on the range of the index it will start from the beginning of the list then go to the next element
# then it will loop back to the beginning and go to the next bigger element
# it will keep getting bigger and bigger until you reach the end of the list

for i in range(len(numbers)):
    print(numbers[0:i])

# example will based on the number list get a group of 3 in every possible list
# not including 8,9,0 don't want that
# would be like 0-2, 1-3, 2-4, etc

# This example will get the list of numbers in a group of 3
# it starts from current index and then adds 3 to that index to get the range
# however it still gives us that leftover range of 8-9, 9

for j in range(len(numbers)):
    print(numbers[j:j+3])

# To fix that leftover range can just add a -2 to the for loop
# the problem is that you don't want to hardcode in numbers

for k in range(len(numbers)-2):
    print(numbers[k:k+3])

# let's say we want a group of 4 numbers with same conditions applied
# There will be 3 leftover numbers instead of 2 so the -2 won't be enough
# There is a relationship here where the correct grouped numbers will always be 1 more bigger than the offset group
# So if I have 4 numbers in the group I need to do -3
# if I have 5 numbers in the group I need to do - 2

for l in range(len(numbers)-2):
    print(numbers[l:l+3])

# it's time to make it dynamic so it can be updated on the fly depending on the list
# first we want a variable for the how much elements needs to be in one group
# then we use that element and subtract it by 1 because we know that the grouped numbers need to be bigger than the offset group
# by 1
# with that all the conditions have been fullfilled

index_size = 3
for o in range(len(numbers)-(index_size-1)):
    print(numbers[o:o+index_size])