# a string

top_commanders = "shiryu, katakuri, king, marco, beckman"
print(top_commanders)

# going to be using split to seperate a string into different parts
# the split itself is descided by the delimiter
# delimiter can be a point in the string you want to use as the split point
# in this example the delimiter will be ", " meaning it will split the string into 5 parts
# the delimiter in a csv file is always a ","

j = top_commanders.split(", ")
print(j)

# you can also make the delimiter into a specific part of the string itself
# in this example the delimiter will be "king" so I should get 2 parts

h = top_commanders.split("king")
print(h)

# going to be using join to combine different substrings together into one full string
# the join function itself ask for what you want as the delimiter
# using the join function will replace the delimiter you have set up in the original string
# so if original delimiter was space then you use , as the join then it will replace that space with a ,
# in other words it replaces the delimiter of a string

b = ",".join(j)
print(b)