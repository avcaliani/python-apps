"""
@author     Anthony Vilarim Caliani
@github     github.com/avcaliani
"""

students = ["Anthony", "Raquel", "Joe", "Nina"]

print(students[0])      # Anthony
print(students[:3])     # ['Anthony C.', 'Raquel', 'Joe']

print(len(students)) # 4
students.append("Daniel")
print(len(students)) # 5

students[0] = "Anthony C."
print(students)  # ['Anthony C.', 'Raquel', 'Joe', 'Nina', 'Daniel']

del students[3]
print(students)  # ['Anthony C.', 'Raquel', 'Joe', 'Daniel']
