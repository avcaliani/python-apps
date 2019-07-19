from core.executor import Executor
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'

class Main:
    def __init__(self):
        self.ex = Executor()

    def run(self):
        print("Wellcome to Py Cryptocurrency \\o/")
        print("Developed by Anthony Caliani (github.com/avcaliani)")
        print("Type 'help' to see commands list. If you want to exit type 'exit'")

        while True:
            command = input("$ ")
            if command.strip() == "exit":
                break
            if command.strip() == "":
                continue
            self.ex.execute(command)

# RUNNING CODE
Main().run()
