# Empty list
x = []

# List with initial values
y = [1, 2, 3, 4, 5]

# List with mixed types
z = [1, "hello", 3.14, True]




# Add element:
z.append(8)

# Sort list ascending:
y.sort()


minVal = y[0]

for i in y:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)