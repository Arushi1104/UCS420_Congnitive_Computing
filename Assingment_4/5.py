import numpy as np

ucs420_arushi=np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])
print("3x4 matrix: ", ucs420_arushi.shape)

mean=np.mean(ucs420_arushi)
print("mean: ", mean)

median=np.median(ucs420_arushi)
print("median: ", median)

max_val=np.max(ucs420_arushi)
print("max value: ", max_val)

min_val=np.min(ucs420_arushi)
print("min value: ", min_val)

unique_val=np.unique(ucs420_arushi)
print("unique values: ", unique_val)

reshaped_ucs420_arushi=ucs420_arushi.reshape(4,3)
print("reshaped array: ", reshaped_ucs420_arushi)

resized_ucs420_arushi=np.resize(ucs420_arushi, (2, 3))
print("resized array: ", resized_ucs420_arushi)