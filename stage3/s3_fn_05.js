// S3_FN_05 — Higher-order predicate
const atLeast = (min) => (n) => n >= min;

// Test with filter
const nums = [1, 5, 10, 15];

const result = nums.filter(atLeast(10));
console.log(result); // [10, 15]
