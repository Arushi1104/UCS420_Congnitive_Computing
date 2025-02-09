import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y1 = x**2
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(np.abs(x) + 1)

plt.figure(figsize=(12, 8))

# Plot Y = x²
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("Y = x²")
plt.xlabel("x")
plt.ylabel("Y")
plt.grid(True)

# Plot Y = sin(x)
plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title("Y = sin(x)")
plt.xlabel("x")
plt.ylabel("Y")
plt.grid(True)

# Plot Y = e^x
plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title("Y = e^x")
plt.xlabel("x")
plt.ylabel("Y")
plt.grid(True)

# Plot Y = log(|x| + 1)
plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title("Y = log(|x| + 1)")
plt.xlabel("x")
plt.ylabel("Y")
plt.grid(True)

plt.tight_layout()
plt.show()
