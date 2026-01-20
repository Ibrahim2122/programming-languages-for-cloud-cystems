// S2_FOR_06 — Nested arrays
function sumNested(matrix) {
  let sum = 0;

  for (const row of matrix) {
    for (const value of row) {
      sum += value;
    }
  }

  return sum;
}

// Tests
console.log(
  sumNested([
    [1, 2],
    [3, 4],
  ]),
); // 10
console.log(sumNested([[5], [10, 15]])); // 30
console.log(sumNested([])); // 0
