import numpy as np
import matplotlib.pyplot as plt

# Simulate energy consumption over time
time = np.arange(0, 24, 0.5)
energy_consumption = 50 * np.sin(0.5 * time) + 100

plt.plot(time, energy_consumption, label='Energy Consumption')
plt.xlabel('Time (hours)')
plt.ylabel('Energy (kWh)')
plt.title('Energy Consumption Over 24 Hours')
plt.legend()
plt.show()
