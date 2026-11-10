//* RSA
// Calculates (base ^ exponent) % modulus
function modPow(base: number, exponent: number, modulus: number): number {
  let result = 1;

  base = base % modulus;

  while (exponent > 0) {
    if (exponent % 2 === 1) {
      result = (result * base) % modulus;
    }

    exponent = Math.floor(exponent / 2);
    base = (base * base) % modulus;
  }

  return result;
}

// Calculates the greatest common divisor
function gcd(a: number, b: number): number {
  while (b !== 0) {
    const temp = b;
    b = a % b;
    a = temp;
  }

  return a;
}

// Finds modular multiplicative inverse
function modInverse(e: number, phi: number): number {
  for (let d = 1; d < phi; d++) {
    if ((e * d) % phi === 1) {
      return d;
    }
  }

  throw new Error("Modular inverse not found");
}

// Generates RSA keys
function generateRSAKeys(p: number, q: number) {
  const n = p * q;
  const phi = (p - 1) * (q - 1);
  // console.log("phi:", phi);

  // Choose public exponent
  let e = 3;

  while (gcd(e, phi) !== 1) {
    e += 2;
  }

  // Calculate private exponent
  const d = modInverse(e, phi);

  return {
    publicKey: { e, n },
    privateKey: { d, n },
  };
}

// Encrypts a numeric message
function encrypt(message: number, publicKey: { e: number; n: number }): number {
  return modPow(message, publicKey.e, publicKey.n);
}

// Decrypts a numeric message
function decrypt(ciphertext: number, privateKey: { d: number; n: number }): number {
  return modPow(ciphertext, privateKey.d, privateKey.n);
}

const p = 11;
const q = 13;

// Generate keys
const keys = generateRSAKeys(p, q);

console.log("Public key:", keys.publicKey);
console.log("Private key:", keys.privateKey);

// Original message
const message = 42;

// Encrypt
const encrypted = encrypt(message, keys.publicKey);

// Decrypt
const decrypted = decrypt(encrypted, keys.privateKey);

console.log("Original message:", message);
console.log("Encrypted message:", encrypted);
console.log("Decrypted message:", decrypted);
