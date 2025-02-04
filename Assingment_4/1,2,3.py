import numpy as np

# # Q1
# a=np.array([10, 13, 16, 1, 12])
# b=a+2
# c=a*3
# d=a/2
# # Q1a
# print("adding 2 to all the elements of the array: ",b)

# # Q1b
# print("multiply 3 with all the elements of the array: ", c)

# # Q1c
# print("dividing all the elements of the array by 2: ", d)

# # Q2a
# arr=np.array([1,2,3,6,4,5])
# arr_reverse=arr[::-1]
# print(arr_reverse)

# Q2b
x = np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])

most = np.bincount(x).argmax()
print("number appering the most in array x: ", most)
index1=np.where(x == most)[0]
print(f"indecies of the number {most} in array x are {index1}")

most1=np.bincount(y).argmax()
print("number appering the most in array y: ", most1)
index2=np.where(y == most1)[0]
print(f"indecies of the number {most1} in array y are {index2}")
# # Q3
# arr1=np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# # Q3a
# print("1st row, 2nd col: ", arr1[0, 1])

# # Q3b
# print("3nd row, 1st col: ", arr1[2, 0])
