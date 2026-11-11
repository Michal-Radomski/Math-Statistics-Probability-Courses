function calculateStatistics(data: number[]) {
  if (data.length === 0) {
    throw new Error("Dataset cannot be empty");
  }

  const sorted = [...data].sort((a, b) => a - b);
  const n = sorted.length;

  // Mean
  const mean: number = sorted.reduce((sum, value) => sum + value, 0) / n;

  // Median
  function median(values: number[]): number {
    const length = values.length;
    const middle = Math.floor(length / 2);

    if (length % 2 === 0) {
      return (values[middle - 1]! + values[middle]!) / 2;
    }

    return values[middle] as number;
  }

  const medianValue: number = median(sorted);

  // Mode
  const frequency = new Map<number, number>();

  sorted.forEach((value) => {
    frequency.set(value, (frequency.get(value) ?? 0) + 1);
  });

  const maxFrequency: number = Math.max(...frequency.values());

  const mode: number[] =
    maxFrequency > 1 ? [...frequency.entries()].filter(([_, count]) => count === maxFrequency).map(([value]) => value) : [];

  // Variance (Population)
  const variance: number = sorted.reduce((sum, value) => sum + Math.pow(value - mean, 2), 0) / n;

  // Standard deviation (Population)
  const standardDeviation: number = Math.sqrt(variance);

  // Range
  const range = sorted[n - 1]! - sorted[0]!;

  // Quartiles
  const middle: number = Math.floor(n / 2);

  const lowerHalf: number[] = sorted.slice(0, middle);
  const upperHalf: number[] = sorted.slice(n % 2 === 0 ? middle : middle + 1);

  const Q1: number = median(lowerHalf);
  const Q2: number = medianValue;
  const Q3: number = median(upperHalf);

  // Interquartile Range
  const IQR = Q3 - Q1;

  return {
    mean,
    median: medianValue,
    mode,
    variance,
    standardDeviation,
    range,
    quartiles: {
      Q1,
      Q2,
      Q3,
    },
    IQR,
  };
}

// Example usage
const data: number[] = [12, 15, 18, 18, 20, 22, 25, 28, 30, 32];

const results = calculateStatistics(data);

console.log("results:", results);
