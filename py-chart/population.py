import data.mock as mock
import matplotlib.pyplot as chart
"""
Further Information
- https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
"""
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'


# Chart Personalization
chart.title("Population Growth")
chart.xlabel("Year")
chart.ylabel("Population (10^8)")

dataset = mock.population()
chart.plot(
    dataset["x"],
    dataset["y"],
    color = dataset["color"]
)

# Running
chart.show()
