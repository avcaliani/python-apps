# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani

# Generic
try:
    if name > 3:  # It will throw an exception!
        print("Wow!")
except:
    print("Exception!")

# Less generic
def defuse_bomb():
    raise Exception("An explosion has occurred!")

try:
    defuse_bomb()
except Exception as e:
    print("Exception! %s" % str(e))