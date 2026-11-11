type Observation = {
  x: number;
  y: number;
};

function calculateBivariateStatistics(data: Observation[]) {
  const n = data.length;

  if (n < 2) {
    throw new Error("At least two observations are required");
  }

  const meanX = data.reduce((sum, item) => sum + item.x, 0) / n;

  const meanY = data.reduce((sum, item) => sum + item.y, 0) / n;

  let covarianceSum = 0;
  let squaredX = 0;
  let squaredY = 0;

  for (const item of data) {
    const dx = item.x - meanX;
    const dy = item.y - meanY;

    covarianceSum += dx * dy;

    squaredX += dx * dx;
    squaredY += dy * dy;
  }

  // Population covariance
  const covariance = covarianceSum / n;

  // Population standard deviations
  const standardDeviationX = Math.sqrt(squaredX / n);
  const standardDeviationY = Math.sqrt(squaredY / n);

  // Pearson correlation
  const denominator = Math.sqrt(squaredX * squaredY);

  if (denominator === 0) {
    throw new Error("Pearson correlation is undefined");
  }

  const pearsonCorrelation = covarianceSum / denominator;

  return {
    observations: n,

    meanX,
    meanY,

    covariance,

    standardDeviationX,
    standardDeviationY,

    pearsonCorrelation,
  };
}

// Example dataset
const data: Observation[] = [
  { x: 1, y: 50 },
  { x: 2, y: 55 },
  { x: 3, y: 65 },
  { x: 4, y: 70 },
  { x: 5, y: 80 },
];

// Calculate statistics
const results = calculateBivariateStatistics(data);

console.log("results:", results);
