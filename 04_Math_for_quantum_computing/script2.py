import cmath


def rect_to_euler(z):
    """Converts a complex number to its Euler/exponential string form: r * e^(i*theta)"""
    r = abs(z)  # Magnitude (modulus)
    theta = cmath.phase(z)  # Phase (argument in radians)

    # Formatting the output string (rounding to 3 decimal places for readability)
    return f"{r:.3f} * e^(i * {theta:.3f})"


# --- Testing the function ---
# Example 1: 1 + 1j
z1 = 1 + 1j
print(f"Rectangular: {z1}  -->  Euler Form: {rect_to_euler(z1)}")

# Example 2: 3 + 4j
z2 = 3 + 4j
print(f"Rectangular: {z2} -->  Euler Form: {rect_to_euler(z2)}")

# Example 3: Pure imaginary (0 + 1j)
z3 = 1j
print(f"Rectangular: {z3}   -->  Euler Form: {rect_to_euler(z3)}")
