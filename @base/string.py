#
# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani
#

# Situation I
sentence = "%s is 21 years old"
name = "Anthony"
print(sentence%name)            # Anthony is 21 years old
print(sentence%("Anthony"))     # Anthony is 21 years old

# Situation II
sentence = "%s is %d years old"
name, age = "Anthony", 21
print(sentence%(name, age))     # Anthony is 21 years old