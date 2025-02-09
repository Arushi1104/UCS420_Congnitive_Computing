import numpy as np
import matplotlib as plt
image=np.random.randint(0, 256, size=(3,3))
print(image)
sobel_x=np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
soble_y=np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

dot=np.dot(image, sobel_x)
print(dot)

normalized_edge = (dot - dot.min()) / (dot.max() - dot.min()) * 255
normalized_edge = normalized_edge.astype(int)
print("normalized: ", normalized_edge)

edge_strength=normalized_edge.sum(axis=1)
strongest_edge_row=np.argmax(edge_strength)
print("strongest edge row: ", strongest_edge_row)

plt.bar()
plt.xlabel("Row Index")
plt.ylabel("Edge Strength")
plt.title("Edge Strength per Row")
plt.show()
