import numpy as np
import matplotlib.pyplot as plt

# input a value for M
M = float(input("Enter a value for M: "))

# Generate x values from -10 to 10 using np.linspace()
x = np.linspace(-10, 10, 400)

# Compute y values 
y1 = M * x**2
y2 = M * np.sin(x)

# Plot both functions in a single figure
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y = M⋅x²', color='blue', linestyle='-')
plt.plot(x, y2, label='y = M⋅sin(x)', color='red', linestyle='--')

# Add legend, grid, and title
plt.legend()
plt.grid(True)
plt.title('Plot of y = M⋅x² and y = M⋅sin(x)')

plt.show()
