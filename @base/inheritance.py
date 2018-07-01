"""
@author     Anthony Vilarim Caliani
@github     github.com/avcaliani
"""

class Parent:
    def __init__(self):
        print("Parent.__init__()")
    
    @staticmethod
    def whoami():
        print("The Boss!")

    def hello(self):
        print("Parent.hello()")
    
    def call_parent(self):
        print("Parent.call_parent()")

    def __del__(self):
        print("Parent.__del__()")


class Child(Parent):
    def __init__(self):
        print("Child.__init__()")

    def hello(self):
        super().hello()
        print("Child.hello()")
    
    def __del__(self):
        print("Child.__del__()")


# Testing
Parent.whoami() # Static
parent = Parent()
parent.hello()

print("-------------------------")

Child.whoami() # Static
child = Child()
child.hello()
child.call_parent()

print("-------------------------")

"""
OUTPUT
anthony@MacBook:@base$ python3 inheritance.py

The Boss!
Parent.__init__()
Parent.hello()
-------------------------
The Boss!
Child.__init__()
Parent.hello()
Child.hello()
Parent.call_parent()
-------------------------
Parent.__del__()
Child.__del__()
"""