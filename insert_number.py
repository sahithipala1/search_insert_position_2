x = [1, 4, 2, 3, 5, 8, 7, 6]
target = 10
x.sort()
y = x.index(5)
print(y)
print(x)
if target in x:
    print(x.index(5))
else:
    print("it is not in array")
