#
# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani
#

students = ["Anthony", "Raquel", "Joe", "Nina"]
fruits = ("Apple", "Banana", "Tomato")

print("# Fruits")
for item in fruits:         # for item in students:
    print(" * %s" % item)

print("\n# Students")
i, max = 0, len(students)
while i < max:
    print(" * %s" % students[i])
    i += 1

print("\n# Range")
for i in range(0, 10):
    print(" * %d" % i)

print("\n# Range + Skip")
for i in range(0, 10, 2):
    print(" * %d" % i)