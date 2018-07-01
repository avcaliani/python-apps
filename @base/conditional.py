"""
@author     Anthony Vilarim Caliani
@github     github.com/avcaliani

Operators:
[ "<", ">", "<=", ">=", "==", "!=" "not", "and", "or" ] 
"""

age = 21

if age < 18:
    print("%d is minor than 18")
elif age >= 18 and age <= 40:
    print("18 <= %d <= 40")
else:
    print("%d is higher than 40")

if not(-1 == 1):
    print("'not' works!")