# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani

numbers = [1, 2, 3]

# Lambda
sum = lambda x, y : x + y

# Map
out_map = map(lambda x : x*2, numbers)

# Filter
out_filter = filter(lambda x : x % 2 == 0, numbers)

print(sum(1, 2))        # 3
print (type(sum))       # <class 'function'>
print(list(out_map))    # [2, 4, 6]
print(list(out_filter)) # [2]
