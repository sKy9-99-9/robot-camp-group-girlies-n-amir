import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [1.2, 0.8, 0, 2.3, 1.9, 0.7, 0.2, 2.4, 2, 1, 0.6, 0.5, 0.9]
y = [0.932, 0.7174, 0, 0.7457, 0.9463, 0.6442, 0.1987, 0.6755, 0.9093, 0.8415, 0.5646, 0.4794, 0.7833]


# Sine curve
x_line = np.linspace(0, 2.5, 500)   # range that covers your data
y_line = np.sin(x_line)

# Plot scatter + sine
plt.scatter(x, y, label="Data", color="red")
plt.plot(x_line, y_line, label="y = sin(x)", color="blue")

# plot data vs model
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()


