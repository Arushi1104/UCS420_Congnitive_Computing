import numpy as np

#4
arushi = np.linspace(10, 100, 25)
print("array: ", arushi)
print("dimentions: ", arushi.ndim)
print("shape: ", arushi.shape)
print("total elements: ", arushi.size)
print("data type of each element: ", arushi.dtype)
print("total number of nytes consumed: ", arushi.nbytes)

arushi_reshape=arushi.reshape(-1, 1)
print("array after reshape: ", arushi_reshape)

arushi_T=arushi.T
print("array after transpose: ", arushi_T)
# Since there are no rows and columns to swap, arr.T returns the same array.
