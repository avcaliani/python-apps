from pyspark import SparkContext
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'

file = "file:///opt/spark/README.md"  
sc = SparkContext("local", "test_app")

# RDD + File
content = sc.textFile(file).cache()
lines = content.count()
count_a = content.filter(lambda s: 'a' in s).count()
count_b = content.filter(lambda s: 'b' in s).count()

print(f'File        {file}')
print(f'Lines       {content.count()}')
print(f'First Line  {content.first()}')
print(f'"a"s Count  {count_a}')
print(f'"b"s Count  {count_b}')

# RDD + Data
data = [1, 2, 4, 5, 6, 7, 8, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 10, 1, 12]
numbers = sc.parallelize(data)

result = numbers.map(lambda n: n * n)
print(f'result.count = {result.count()}')

print('\n# MAPPING')
for n in result.take(9):
    print(f'-> {n}')


print('\n# FILTERING')
result = numbers.filter(lambda n: n >= 10)
for n in result.collect():
    print(f'-> {n}')


print('\n# REDUCING')
result = numbers.reduce(lambda x, y: x + y)
print(f'sum -> {result}')


print('\n# COUNTING')
result = numbers.countByValue()
for key, value in result.items():
    print(f'{key}: {value}')

print(numbers.top(1))
