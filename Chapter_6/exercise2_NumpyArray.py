import numpy as np

a = np.array([20,23,82,40,32,15,67,52])

x = np.where(a % 2 == 0)

for y in x[0]:
    print(y)

print("This is the array that are sorted:", np.sort(a))
print("This is the array that are sliced from index 3 to the end of the array:", a[3:])
print("This is the array that are sliced from index 0 to 4:", a[0:4])
print("This is the array that prints out the numbers [32 15 67]:", a[-4:-1])