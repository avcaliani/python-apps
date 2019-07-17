import re
from os import path
from functools import reduce
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark.mllib.linalg import Vectors
from pyspark.sql import *
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'

FILE_PATH = f'{ path.dirname(path.abspath(__file__)) }/../data/crimes.csv'

reduce_str = lambda v: float(reduce(
    lambda x, y: x + y, list(bytes(v, 'utf-8'))
))


  # # #    #   #    #   #    #   #    # # #    #   #    # # #
  #   #    #   #    ##  #    ##  #      #      ##  #    #
  # #      #   #    # # #    # # #      #      # # #    #  ##
  #  #     #   #    #  ##    #  ##      #      #  ##    #   #
  #   #    # # #    #   #    #   #    # # #    #   #    # # #


sc = SparkContext("local", "k_means_app")
sql_ctx = SQLContext(sc)

file_content = sc.textFile(FILE_PATH)
data = file_content.map(lambda line: line.split(','))

states = data.map(
    lambda line: { 'state': line[0], 'code': reduce_str(line[0]) }
).toDF()
states.show()
states.createOrReplaceTempView("states")

crimes = data.map(lambda l: Vectors.dense(
    reduce_str(l[0]),   # State
    float(l[2]),        # Murder
    float(l[3]),        # Assault
    float(l[4]),        # Urban Population
    float(l[5])         # Rape
))
clusters = KMeans.train(crimes, 5, 10)

crime_classes = crimes.map(lambda c: {
    'code': float(c[0]),
    'murder': float(c[1]),
    'assault': float(c[2]), 
    'urban_pop': float(c[3]), 
    'rape':float(c[4]),
    'prediction_vector': c,
    'prediction': float(clusters.predict(c))
}).toDF()
crime_classes.show()
crime_classes.createOrReplaceTempView("crimes")

sql_ctx.sql("""
    SELECT
        state, prediction, urban_pop 
    FROM crimes 
        INNER JOIN states ON crimes.code = states.code
""").show(100, False)
