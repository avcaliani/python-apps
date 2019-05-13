# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani
from random import randint

def random(array_size):
    array = []
    for i in range (0, array_size):
        array.append(randint(1, 101))
    return array

def population():
    lines = open("population.csv").readlines()
    x, y = [], []
    for line in lines:
        if line == lines[0]:
            continue
        data = line.split(";")
        x.append(int(data[0]))
        y.append(int(data[1]))
    return {
        "x": x, "y": y, "color": "#20bf6b"
    }

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