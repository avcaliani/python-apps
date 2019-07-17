# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani
#
# @see https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
import mock
import matplotlib.pyplot as chart

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
