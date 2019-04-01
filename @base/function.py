# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani

def hello(name, nickname = None):
    if nickname is not None:
        print("Hello %s (%s)" % (name, nickname))
    else:
        print("Hello %s" % name)


def sum(*args):
    if (len(args) <= 0):
        print("Values not found!")
        return
    total = 0
    for value in args:
        total += value
    print("Total: %d" % total)

def show(**kwargs):
    if (len(kwargs) <= 0):
        print("Nothing to show!")
        return
    
    for key, value in kwargs.items():
        print("%s: %s" % (key, value))
    
    if 'github' in kwargs:
        print("\nCheck my GitHub -> %s" % kwargs.get("github"))


# Testing
hello("Anthony")                    # Hello Anthony
hello("Anthony", "@avcaliani")      # Hello Anthony (@avcaliani)

sum()               # Values not found!
sum(1, 1)           # Total: 2
sum(1, 2, 3, 4, 5)  # Total: 15

show()  # Nothing to show!
show(name="Anthony", age=21)
# name: Anthony
# age: 21

show(name="Anthony", nickname="avcaliani", github="https://github.com/avcaliani")
# name: Anthony
# nickname: avcaliani
# github: https://github.com/avcaliani
#
# Check my GitHub -> https://github.com/avcaliani
