import re
from os import path
from pyspark import SparkContext
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.feature import Normalizer
from pyspark.mllib.regression import LabeledPoint
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'

FILE_PATH = f'{ path.dirname(path.abspath(__file__)) }/../data/tree.data.txt'
CLASS_NUM = 3
CATEGORICAL_FEATURES_INFO = { 6: 3 }
IMPURITY = 'gini'
MAX_DEPTH = 9
MAX_BINS = 7


  # # #    #   #    #   #    #   #    # # #    #   #    # # #
  #   #    #   #    ##  #    ##  #      #      ##  #    #
  # #      #   #    # # #    # # #      #      # # #    #  ##
  #  #     #   #    #  ##    #  ##      #      #  ##    #   #
  #   #    # # #    #   #    #   #    # # #    #   #    # # #


sc = SparkContext("local", "tree_app")
file_content = sc.textFile(FILE_PATH).map(
    lambda line: re.compile('\t').split(line)
)
print(f'file_content.count = { file_content.count() }')

data = file_content.map(
    lambda array: list(map(lambda value: float(value),  array))
).cache()
print(f'data.count = { data.count() }')

points = data.map(
    lambda array: LabeledPoint(
        array.pop(0),  
        Vectors.dense(array)
    )
).cache()

model = DecisionTree.trainClassifier(
    points, CLASS_NUM, CATEGORICAL_FEATURES_INFO , IMPURITY, MAX_DEPTH, MAX_BINS
)

print('\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=')
print(' TREE MODEL')
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\n')
print(model.toDebugString())
print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=')