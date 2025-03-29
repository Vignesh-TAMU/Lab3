import numpy as np
from scipy.signal import freqz
import matplotlib.pyplot as plt

# System parameters
base_freq = 2.4e9
cap_high = 15.425e-12
cap_reg = 0.5e-12

# Calculate coefficients
alpha = cap_high / (cap_high + cap_reg)
print(f"Alpha value: {alpha}")
scale_factor = 1 / (2 * base_freq * (cap_reg + cap_high))

# First numerator setup
base_num = scale_factor * np.ones(8)
zeros_pad = np.zeros(17)
combined_num = np.concatenate([base_num, zeros_pad])

# Second numerator setup
pattern = [1] + [0]*7 + [alpha] + [0]*7 + [alpha**2] + [0]*7 + [alpha**3]
num_modifier = np.array(pattern)
print(f"Numerator pattern: {num_modifier}")
final_numerator = combined_num * num_modifier

# First denominator (1st IIR)
base_den = np.array([1] + [0]*7 + [-alpha])
den_padding = np.zeros(56)
extended_den = np.concatenate([base_den, den_padding])
print(f"Extended denominator: {extended_den}")

# Second IIR setup
iir2_start = np.array([1])
iir2_zeros = np.zeros(62)
iir2_end = np.array([0, alpha])
iir2_full = np.concatenate([iir2_start, iir2_zeros, iir2_end])
print(f"IIR2 coefficients: {iir2_full}")

# Final denominator
final_denominator = extended_den * iir2_full

# Frequency response
frequencies, response = freqz(final_numerator, final_denominator)

# Plotting
plt.figure()
plt.plot(frequencies, 20 * np.log10(np.abs(response)), 'r', linewidth=1.2)
plt.grid(True)
plt.title('Frequency Response: 4-Capacitor Bank with History Discharge')
plt.xlabel('Frequency (radians/second)')
plt.ylabel('Magnitude (dB)')
plt.show()
