import numpy as np
import matplotlib.pyplot as plt


# Generate a random 3x3 grayscale image
image = np.random.randint(0, 256, size=(3, 3))

print("Original Image:\n", image)

# Sobel filters
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Apply Sobel filters
grad_x = convolve2d(image, sobel_x, mode="same", boundary="fill", fillvalue=0)
grad_y = convolve2d(image, sobel_y, mode="same", boundary="fill", fillvalue=0)

# Compute gradient magnitude
edge_magnitude = np.sqrt(grad_x**2 + grad_y**2)

# Normalize the edge strength to [0, 255]
normalized_edge = (edge_magnitude - edge_magnitude.min()) / (edge_magnitude.max() - edge_magnitude.min()) * 255
normalized_edge = normalized_edge.astype(int)

print("Normalized Edge Magnitude:\n", normalized_edge)

# Sum edge strength for each row
edge_strength = normalized_edge.sum(axis=1)

# Find the row with the strongest edge
strongest_edge_row = np.argmax(edge_strength)
print("Strongest Edge Row:", strongest_edge_row)

# Plot edge strength per row
plt.bar(range(image.shape[0]), edge_strength)
plt.xlabel("Row Index")
plt.ylabel("Edge Strength")
plt.title("Edge Strength per Row")
plt.show()
