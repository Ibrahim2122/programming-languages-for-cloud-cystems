// S2_ARR_02 — Deduplicate
function unique(values) {
  const result = [];

  for (const v of values) {
    if (!result.includes(v)) {
      result.push(v);
    }
  }

  return result;
}

// Tests
console.log(unique([1, 2, 2, 3, 1])); // [1, 2, 3]
console.log(unique(["a", "b", "a", "c"])); // ["a", "b", "c"]
console.log(unique([true, true, false])); // [true, false]
