from math import pow
from os import path
from pyspark import SparkContext
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.feature import Normalizer
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'

FILE_PATH = f'{ path.dirname(path.abspath(__file__)) }/../data/lpsa.data.txt'
NUM_ITERATIONS = 100
STEP_SIZE = 0.00000001

def parse_data(line):
    data = list(map(
        lambda n: float(n), line.replace(',', ' ').split(' ')
    ))
    return LabeledPoint(
        data[0],
        Vectors.dense(data[0], data[ len(data) -1 ])
    )


  # # #    #   #    #   #    #   #    # # #    #   #    # # #
  #   #    #   #    ##  #    ##  #      #      ##  #    #
  # #      #   #    # # #    # # #      #      # # #    #  ##
  #  #     #   #    #  ##    #  ##      #      #  ##    #   #
  #   #    # # #    #   #    #   #    # # #    #   #    # # #


sc = SparkContext("local", "linear_regression_app")

file_content = sc.textFile(FILE_PATH).cache()
print(f'file_content.count = { file_content.count() }')

data = file_content.map(parse_data).cache()
print(f'data.count = { data.count() }')

model = LinearRegressionWithSGD.train(data, NUM_ITERATIONS, STEP_SIZE)
predictions = data.map(
    lambda point: (point.label, model.predict(point.features))
)

predictions.foreach(
    lambda point: print(f"Predicted: { point[0] }\t| Actual: { point[1] }")
)

mse = predictions.map(
    lambda point: pow((point[0] - point[1]), 2)
).mean()
print(f'Training Mean Squared Error = { mse }')
