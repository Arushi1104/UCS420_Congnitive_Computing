import numpy as np

# Q1
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

#i
total = gfg.sum()
print(total)

#ii
row = gfg.sum(axis=1)
print(row)

#iii
colm = gfg.sum(axis=0)
print(colm)

# Q2a
array = np.array([10, 52, 62, 16, 16, 54, 453])

#i
sorted_arr = np.sort(array)
print(sorted_arr)

#ii
sorted_indices = np.argsort(array)
print(sorted_indices)

#iii
smallest_el = np.sort(array)[:4]
print(smallest_el)

#iv
largest_el = np.sort(array)[-5:]
print(largest_el)

# Q2b
array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

#i
int_el = array[array == array.astype(int)]
print(int_el)

#ii
float_el = array[array != array.astype(int)]
print(float_el)