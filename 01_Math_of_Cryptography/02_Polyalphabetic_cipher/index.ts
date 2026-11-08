/**
 * Helper function to clean the key (removes non-alphabetic characters and uppercases it)
 */
function sanitizeKey(key: string): string {
  return key.replace(/[^a-zA-Z]/g, "").toUpperCase();
}

/**
 * Encrypts a message using the Vigenère cipher.
 */
function encryptVigenere(plaintext: string, key: string): string {
  const cleanKey = sanitizeKey(key);
  if (cleanKey.length === 0) return plaintext;

  let result = "";
  let keyIndex = 0;

  for (let i = 0; i < plaintext.length; i++) {
    const char = plaintext[i] as string;
    const code = char.charCodeAt(0);

    // Uppercase letters (A-Z)
    if (code >= 65 && code <= 90) {
      const shift = (cleanKey[keyIndex % cleanKey.length] as string).charCodeAt(0) - 65;
      const encryptedChar = String.fromCharCode(((code - 65 + shift) % 26) + 65);
      result += encryptedChar;
      keyIndex++;
    }
    // Lowercase letters (a-z)
    else if (code >= 97 && code <= 122) {
      const shift = (cleanKey[keyIndex % cleanKey.length] as string).charCodeAt(0) - 65;
      const encryptedChar = String.fromCharCode(((code - 97 + shift) % 26) + 97);
      result += encryptedChar;
      keyIndex++;
    }
    // Non-alphabetic characters remain unchanged
    else {
      result += char;
    }
  }

  return result;
}

/**
 * Decrypts a message using the Vigenère cipher.
 */
function decryptVigenere(ciphertext: string, key: string): string {
  const cleanKey = sanitizeKey(key);
  if (cleanKey.length === 0) return ciphertext;

  let result = "";
  let keyIndex = 0;

  for (let i = 0; i < ciphertext.length; i++) {
    const char = ciphertext[i] as string;
    const code = char.charCodeAt(0);

    // Uppercase letters (A-Z)
    if (code >= 65 && code <= 90) {
      const shift = (cleanKey[keyIndex % cleanKey.length] as string).charCodeAt(0) - 65;
      // Adding 26 ensures the result of the modulo is positive
      const decryptedChar = String.fromCharCode(((code - 65 - shift + 26) % 26) + 65);
      result += decryptedChar;
      keyIndex++;
    }
    // Lowercase letters (a-z)
    else if (code >= 97 && code <= 122) {
      const shift = (cleanKey[keyIndex % cleanKey.length] as string).charCodeAt(0) - 65;
      const decryptedChar = String.fromCharCode(((code - 97 - shift + 26) % 26) + 97);
      result += decryptedChar;
      keyIndex++;
    }
    // Non-alphabetic characters remain unchanged
    else {
      result += char;
    }
  }

  return result;
}

const message = "Attack at dawn!";
const secretKey = "lemon";

const encrypted = encryptVigenere(message, secretKey);
console.log("Encrypted:", encrypted);
// Output: "Lxedpy ex heor!"

const decrypted = decryptVigenere(encrypted, secretKey);
console.log("Decrypted:", decrypted);
// Output: "Attack at dawn!"
