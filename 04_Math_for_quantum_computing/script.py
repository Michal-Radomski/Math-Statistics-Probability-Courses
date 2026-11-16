# 1. Defining complex numbers
z1 = 3 + 4j
z2 = 1 + 2j

print(f"z1 = {z1}")
print(f"z2 = {z2}\n")

# 2. Accessing real and imaginary parts
print("--- Real and Imaginary Parts ---")
print("Real part of z1:", z1.real)  # Output: 3.0
print("Imaginary part of z1:", z1.imag)  # Output: 4.0

# 3. Finding the complex conjugate
print("\n--- Complex Conjugate ---")
print("Conjugate of z1:", z1.conjugate())  # Output: (3-4j)

# 4. Arithmetic Operations
print("\n--- Arithmetic ---")
print("Addition (z1 + z2):", z1 + z2)  # Output: (4+6j)
print("Multiplication (z1 * z2):", z1 * z2)  # Output: (-5+10j)

# 5. Using the 'cmath' module for Euler/Polar notation
import cmath

# Magnitude and Phase (Argument)
magnitude = abs(z1)  # or cmath.polar(z1)[0]
phase = cmath.phase(z1)  # Angle in radians

print("\n--- Polar / Euler Form ---")
print(f"Magnitude of z1: {magnitude}")
print(f"Phase (radians) of z1: {phase}")

# Testing Euler's Identity: e^(i * pi) + 1 = 0
euler_identity = cmath.exp(1j * cmath.pi) + 1
print(f"e^(i * pi) + 1 (approx): {euler_identity}")  # Close to 0 + 0j
