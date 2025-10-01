# Take input from user as space-separated numbers
data = list(map(float, input("Enter numbers separated by spaces: ").split()))

# Sort the data
data.sort()

# Calculate median
n = len(data)
m = n // 2
if n % 2 == 0:
    median = (data[m - 1] + data[m]) / 2
else:
    median = data[m]

print("Median:", median)
