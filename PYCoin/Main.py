import entities.Coin
import core.Executor

class Main:
    def __init__(self):
        self.executor = core.Executor.Executor()

    def run(self):
        print("Wellcome to PYCoin \\o/")
        print("Developed by Anthony Caliani (github.com/avcaliani)")
        print("Type 'help' to see commands list. If you want to exit type 'exit'")

        while True:
            command = input("pycoin> ")
            if command.strip() == "exit":
                break
            if command.strip() == "":
                continue
            self.executor.execute(command)

# RUNNING CODE
Main().run()
