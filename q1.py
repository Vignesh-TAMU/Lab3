from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt

# Parameters
filter_order = 8
capacitance = 15.925e-12
frequency_base = 2.4e9

# Calculate amplification factor
amp_factor = 0.5 * frequency_base * capacitance

# Define filter coefficients
num_coeffs = amp_factor * np.ones(filter_order)
den_coeffs = np.array([amp_factor])

# Compute frequency response
frequencies, transfer_function = freqz(num_coeffs, den_coeffs)

# Create plot
plt.figure()
plt.plot(frequencies, 20 * np.log10(np.abs(transfer_function)), 'r', linewidth=1.5)
plt.grid(True)
plt.title('Magnitude Response of Discharged Capacitor - Case 1 (UIN534001737)')
plt.xlabel('Frequency (radians/sec)')
plt.ylabel('Magnitude (dB)')
plt.show()
