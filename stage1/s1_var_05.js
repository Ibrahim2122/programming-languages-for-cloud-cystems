// S1_VAR_05 — Array vs object
function isArray(value) {
  return Array.isArray(value);
}

// Tests
console.log(isArray([])); // true
console.log(isArray([1, 2, 3])); // true
console.log(isArray({})); // false
console.log(isArray({ a: 1 })); // false
console.log(isArray(null)); // false
