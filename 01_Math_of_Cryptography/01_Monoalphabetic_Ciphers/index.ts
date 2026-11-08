/**
 * Calculates the Greatest Common Divisor (GCD) of two integers
 * using the iterative Euclidean algorithm.
 *
 * @param a - The first integer
 * @param b - The second integer
 * @returns The greatest common divisor of a and b
 */
function gcd(a: number, b: number): number {
  // Work with absolute values to handle negative numbers safely
  let x = Math.abs(a);
  let y = Math.abs(b);

  // Repeatedly take the remainder until y becomes 0
  while (y !== 0) {
    const remainder = x % y;
    x = y;
    y = remainder;
  }

  return x;
}

console.log("gcd(48, 56):", gcd(48, 56)); //* -> 8
console.log("gcd(795, 539):", gcd(795, 539)); //* -> 1 - coprime number
