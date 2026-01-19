// S1_VAR_06 — NaN pitfalls
function classifyNumberLike(x) {
  if (Number.isNaN(x)) return "nan";
  if (typeof x === "number") return "number";
  return "not-a-number";
}

// Tests
console.log(classifyNumberLike(NaN)); // "nan"
console.log(classifyNumberLike(0)); // "number"
console.log(classifyNumberLike("0")); // "not-a-number"
console.log(classifyNumberLike("abc")); // "not-a-number"
console.log(classifyNumberLike(undefined)); // "not-a-number"
