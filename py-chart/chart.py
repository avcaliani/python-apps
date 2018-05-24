import data.mock as mock
import matplotlib.pyplot as chart
"""
Further Information
- https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
"""

# Chart Personalization
chart.title("My Random Chart")

chart.xlabel("Rand X Label")
chart.ylabel("Rand Y Label")

# Available Charts:
# Line      -> chat.plot(...)
# Bar       -> chat.bar(...)
# Scatter   -> chat.scatter(...)
for dataset in mock.datasets:
    chart.scatter(
        dataset["x"],
        dataset["y"],
        label = dataset["name"],
        color = dataset["color"]
    )
chart.legend()

# Running
chart.show()

# Saving chart as file
# Supported Formats: eps, pdf, pgf, png, ps, raw, rgba, svg, svgz
# chart.savefig("chart.pdf")
