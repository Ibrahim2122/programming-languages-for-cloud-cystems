// S3_FN_04 — Map / filter / reduce with arrows
const nums = [1, 2, 3, 4, 5, 6];

const sumOfSquaresOfEvens = nums
  .filter((n) => n % 2 === 0)
  .map((n) => n * n)
  .reduce((sum, n) => sum + n, 0);

// Test
console.log(sumOfSquaresOfEvens); // 56 (4 + 16 + 36)
