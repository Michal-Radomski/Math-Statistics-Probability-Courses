/**
 * Calculates the Greatest Common Divisor (GCD) of two integers
 * using the iterative Euclidean algorithm.
 *
 * @param a - The first integer
 * @param b - The second integer
 * @returns The greatest common divisor of a and b
 */
// function gcd(a: number, b: number): number {
//   // Work with absolute values to handle negative numbers safely
//   let x = Math.abs(a);
//   let y = Math.abs(b);

//   // Repeatedly take the remainder until y becomes 0
//   while (y !== 0) {
//     const remainder = x % y;
//     x = y;
//     y = remainder;
//   }

//   return x;
// }

// console.log("gcd(48, 56):", gcd(48, 56)); //* -> 8
// console.log("gcd(795, 539):", gcd(795, 539)); //* -> 1 - coprime number

// Helper function: Extended Euclidean Algorithm to find modular inverse
function extendedGcd(a: number, b: number): [number, number, number] {
  if (b === 0) return [a, 1, 0];
  const [gcd, x1, y1] = extendedGcd(b, a % b);
  const x = y1;
  const y = x1 - Math.floor(a / b) * y1;
  return [gcd, x, y];
}

// Find modular multiplicative inverse of a modulo m
function modInverse(a: number, m: number): number {
  const [gcd, x] = extendedGcd(a, m);
  if (gcd !== 1) {
    throw new Error(`Modular inverse does not exist because gcd(${a}, ${m}) !== 1. 'a' must be coprime to 26.`);
  }
  return ((x % m) + m) % m;
}

/**
 * Encrypts a plaintext string using the Affine Cipher.
 * Formula: E(x) = (a * x + b) mod 26
 */
function encryptAffine(plaintext: string, a: number, b: number): string {
  const m = 26;
  let result = "";

  for (let i = 0; i < plaintext.length; i++) {
    const char = plaintext[i] as string;

    if (char >= "a" && char <= "z") {
      const x = char.charCodeAt(0) - 97; // 'a' is 97
      const encryptedCode = (((a * x + b) % m) + m) % m;
      result += String.fromCharCode(encryptedCode + 97);
    } else if (char >= "A" && char <= "Z") {
      const x = char.charCodeAt(0) - 65; // 'A' is 65
      const encryptedCode = (((a * x + b) % m) + m) % m;
      result += String.fromCharCode(encryptedCode + 65);
    } else {
      result += char; // Keep non-alphabetic characters as-is
    }
  }

  return result;
}

/**
 * Decrypts a ciphertext string using the Affine Cipher.
 * Formula: D(y) = a^-1 * (y - b) mod 26
 */
function decryptAffine(ciphertext: string, a: number, b: number): string {
  const m = 26;
  const aInverse = modInverse(a, m);
  let result = "";

  for (let i = 0; i < ciphertext.length; i++) {
    const char = ciphertext[i] as string;

    if (char >= "a" && char <= "z") {
      const y = char.charCodeAt(0) - 97;
      const decryptedCode = (((aInverse * (y - b)) % m) + m) % m;
      result += String.fromCharCode(decryptedCode + 97);
    } else if (char >= "A" && char <= "Z") {
      const y = char.charCodeAt(0) - 65;
      const decryptedCode = (((aInverse * (y - b)) % m) + m) % m;
      result += String.fromCharCode(decryptedCode + 65);
    } else {
      result += char;
    }
  }

  return result;
}

// --- Example Usage ---
const message = "Hello, World!";
const a = 5;
const b = 8;

const encrypted = encryptAffine(message, a, b);
const decrypted = decryptAffine(encrypted, a, b);

console.log(`Original:  ${message}`); //* Hello, World!
console.log(`Encrypted: ${encrypted}`); //* Rclla, Oaplx!
console.log(`Decrypted: ${decrypted}`); //* Hello, World!
