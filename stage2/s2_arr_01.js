// S2_ARR_01 — Clean numbers
function cleanNumbers(arr) {
  return arr
    .map((s) => +s) // convert strings to numbers
    .filter((n) => !Number.isNaN(n)); // drop NaN values
}

// Example test
console.log(cleanNumbers([" 1 ", "x", "2"])); // [1, 2]

// More tests
console.log(cleanNumbers(["10", " 3.5 ", "abc", ""])); // [10, 3.5, 0]
