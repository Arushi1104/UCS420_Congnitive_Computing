import numpy as np
import matplotlib.pyplot as plt

roll_number = 102317147  
np.random.seed(roll_number)

data = np.random.randn(50)

# Create a 2x2 subplot layout
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Line plot showing cumulative sum
axs[0, 0].plot(np.cumsum(data), marker='o', linestyle='-', color='b')
axs[0, 0].set_title('Cumulative Sum Plot')
axs[0, 0].set_xlabel('Index')
axs[0, 0].set_ylabel('Cumulative Sum')
axs[0, 0].grid(True)

# Scatter plot with random noise
noise = np.random.randn(50)
axs[0, 1].scatter(data, noise, color='r', marker='x')
axs[0, 1].set_title('Scatter Plot with Random Noise')
axs[0, 1].set_xlabel('Data')
axs[0, 1].set_ylabel('Noise')
axs[0, 1].grid(True)

# Hide the other subplots
axs[1, 0].axis('off')
axs[1, 1].axis('off')

# Add a main title for the entire figure
fig.suptitle('2x2 Subplot Layout with Cumulative Sum and Scatter Plot', fontsize=16)

# Adjust the layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()
