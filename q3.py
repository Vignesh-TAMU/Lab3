import numpy as np
from scipy.signal import freqz
import matplotlib.pyplot as plt

# Constants
frequency = 2.4e9
capacitance_high = 15.295e-12
capacitance_regular = 0.5e-9

# Calculations
alpha = capacitance_high / (capacitance_high + capacitance_regular)
amplification = 0.5 * frequency * capacitance_regular

# Filter coefficients
top_coeffs = amplification * np.ones(16)
bottom_coeffs = np.array([1] + [0]*7 + [-alpha])

# Frequency response calculation
frequencies, response = freqz(top_coeffs, bottom_coeffs)

# Plotting
plt.figure()
plt.plot(frequencies, 20 * np.log10(np.abs(response)), 'r')
plt.grid(True)
plt.xlabel('Frequency (radians/second)')
plt.ylabel('Magnitude (decibels)')
plt.title('Frequency Response with 4 Discharged Capacitors')
plt.show()
