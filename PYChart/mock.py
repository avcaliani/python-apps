# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani
from random import randint

def random(array_size):
    array = []
    for i in range (0, array_size):
        array.append(randint(1, 101))
    return array

# Chart Data
datasets = (
    {
        "x": random(15),
        "y": random(15),
        "name": "Set-A",
        "color": "#20bf6b"
    },
    {
        "x": random(15),
        "y": random(15),
        "name": "Set-A",
        "color": "#3867d6"
    }
)