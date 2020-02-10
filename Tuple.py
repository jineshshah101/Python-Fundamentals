# a tuple looks just like a list except it surrounded by () instead of []
# [] means list
# () means tuple

g = (1,2,3)

# can print the index of a element in a tuple just like a list

print(g[0])

# tuples cannot be changed
# cannot add elements, remove elements, can't change things within it
# tuples are more stable and secure

# for example handling credit card information requires the elements to be stable and secure and cannot be changed

credit_card1 = (1234123412341234, "Edward Newgate", "05/25", 234)
credit_card2 = (2345234523452345, "Gold Roger", "11/20", 456)

# you can put multiple tuples together as a list or a list of tuples

credit_card_list = (credit_card1, credit_card2)
print(credit_card_list)

# unpacking a tuple
# take elements inside the tuple and unpack it into seperate elements
# that way you can get each elements of a tuple be printed out seperately

(credit_card_number, name, expDate, cv) = credit_card1
print(credit_card_number)
print(name)
print(expDate)
print(cv)

# can iterate over a list of tuples which can be used with unpacking

RedHair = ("Shanks", 4048900000, "NA", "Ben Beckman")
BlackBeard = ("Teach", 2247600000, "Darkness + Quake", "Shiryu")
BigMom = ("Linlin", 4388000000, "Souls", "Katakuri")
BeastPirates = ("Kaido", 4611100000, "Dragon", "King")
Emperors = [BlackBeard, RedHair, BigMom, BeastPirates]

for Name, bounty, devilfruit, righthand in Emperors:
    print(Name)
    print(bounty)
    print(devilfruit)
    print(righthand)
    print()


