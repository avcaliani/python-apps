#
# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani
#

students = { "Anthony":20, "Raquel":20, "Nina": 18 }

print(students)  # {'Anthony': 20, 'Raquel': 20, 'Nina': 18}
print(students["Anthony"])  # 20

# Updating Student Age
students["Anthony"] = 21
print(students)  # {'Anthony': 21, 'Raquel': 20, 'Nina': 18}

# Removing Student
del students["Nina"]
print(students)  # {'Anthony': 21, 'Raquel': 20}

# New Student
students["Bob"] = 25
print(students)  # {'Anthony': 21, 'Raquel': 20, 'Bob': 25}
