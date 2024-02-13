import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equation function
def model(y, t):
    k = 0.3  # Example parameter
    dydt = -k * y  # Example differential equation (dy/dt = -k*y)
    return dydt

# Define the time points
t = np.linspace(0, 20, 100)  # 100 time points from 0 to 20

# Solve the differential equation
y0 = 5  # Initial condition
y = odeint(model, y0, t)

# Plot the results
plt.plot(t, y, 'r', label='y(t)')  # 'r' for red line
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Differential Equation Visualization')
plt.legend()
plt.show()
