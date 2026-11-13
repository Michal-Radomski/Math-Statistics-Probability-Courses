function createSeededRandom(seed: number): () => number {
  let state = seed;
  return function (): number {
    // Numerical Recipes LCG constants
    state = (state * 1664525 + 1013904223) % 4294967296;
    return state / 4294967296; // Returns a float between 0 and 1
  };
}

// Equivalent to random.seed(123)
const rng: () => number = createSeededRandom(123);

console.log(1, "rng():", rng()); // Always produces the same value for seed 123
console.log(2, "rng():", rng());
console.log(3, "rng():", rng());
