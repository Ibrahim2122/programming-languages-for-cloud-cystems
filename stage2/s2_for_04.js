// S2_FOR_04 — Count occurrences
function countOccurrences(values) {
  const counts = {};

  for (const v of values) {
    const key = String(v);
    counts[key] = (counts[key] || 0) + 1;
  }

  return counts;
}

// Tests
console.log(countOccurrences([1, 2, 1, 3, 2, 1]));
// { '1': 3, '2': 2, '3': 1 }

console.log(countOccurrences(["a", "b", "a"]));
// { a: 2, b: 1 }
