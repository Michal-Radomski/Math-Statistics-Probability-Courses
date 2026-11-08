const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const ROTORS = {
  I: {
    wiring: "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    notch: "Q",
  },
  II: {
    wiring: "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    notch: "E",
  },
  III: {
    wiring: "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    notch: "V",
  },
};

const REFLECTOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT";

class Enigma {
  private positions = [0, 0, 0];

  constructor(
    private rotors: string[] = ["I", "II", "III"],
    initialPositions: string = "AAA"
  ) {
    this.positions = [...initialPositions].map((char) => alphabet.indexOf(char));
  }

  private rotate() {
    // Simplified stepping mechanism
    this.positions[2] = (this.positions[2]! + 1) % 26;

    if (this.positions[2] === 0) {
      this.positions[1] = (this.positions[1]! + 1) % 26;
    }

    if (this.positions[1] === 0) {
      this.positions[0] = (this.positions[0]! + 1) % 26;
    }
  }

  private forward(index: number, rotor: string, position: number): number {
    const wiring = ROTORS[rotor as keyof typeof ROTORS].wiring;

    const shifted = (index + position) % 26;
    const mapped = alphabet.indexOf(wiring[shifted]!);

    return (mapped - position + 26) % 26;
  }

  private backward(index: number, rotor: string, position: number): number {
    const wiring = ROTORS[rotor as keyof typeof ROTORS].wiring;

    const shifted = (index + position) % 26;
    const mapped = wiring.indexOf(alphabet[shifted]!);

    return (mapped - position + 26) % 26;
  }

  private encryptCharacter(char: string): string {
    let index = alphabet.indexOf(char);

    if (index === -1) return char;

    this.rotate();

    // Forward through rotors
    for (let i = 2; i >= 0; i--) {
      index = this.forward(index, this.rotors[i]!, this.positions[i]!);
    }

    // Reflector
    index = alphabet.indexOf(REFLECTOR[index]!);

    // Backward through rotors
    for (let i = 0; i < 3; i++) {
      index = this.backward(index, this.rotors[i]!, this.positions[i]!);
    }

    return alphabet[index] as string;
  }

  encrypt(text: string): string {
    return [...text.toUpperCase()].map((char) => this.encryptCharacter(char)).join("");
  }
}

// Encryption
const machine = new Enigma(["I", "II", "III"], "AAA");

const message = "HELLOWORLD";
console.log("message:", message); //* HELLOWORLD

const encrypted = machine.encrypt(message);
console.log("Encrypted:", encrypted); //* YOUVUDCACC

// Decryption
const decryptMachine = new Enigma(["I", "II", "III"], "AAA");

const decrypted = decryptMachine.encrypt(encrypted);
console.log("Decrypted:", decrypted); //* HELLOWORLD
