//* Diffie-Hellman
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

  // console.log("result:", result);
  return result;
}

// Generates public and private keys
function generateKeys(privateKey: number, generator: number, prime: number) {
  const publicKey = modPow(generator, privateKey, prime);

  return {
    privateKey,
    publicKey,
  };
}

// Calculates shared secret
function calculateSharedSecret(otherPublicKey: number, privateKey: number, prime: number): number {
  return modPow(otherPublicKey, privateKey, prime);
}

const prime = 23;
const generator = 5;

// Alice chooses her private key
const alice = generateKeys(6, generator, prime);

// Bob chooses his private key
const bob = generateKeys(15, generator, prime);

// Exchange public keys and calculate shared secrets
const aliceSecret = calculateSharedSecret(bob.publicKey, alice.privateKey, prime);

const bobSecret = calculateSharedSecret(alice.publicKey, bob.privateKey, prime);

console.log("Alice public key:", alice.publicKey);
console.log("Bob public key:", bob.publicKey);

console.log("Alice shared secret:", aliceSecret);
console.log("Bob shared secret:", bobSecret);
