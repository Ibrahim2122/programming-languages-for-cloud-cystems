// S1_VAR_07 — Coercion via unary plus
function toNumberOrNull(x) {
  if (typeof x !== "string") return null;

  const n = +x; // unary plus coercion
  if (Number.isNaN(n)) return null;

  return n;
}

// Tests
console.log(toNumberOrNull("12")); // 12
console.log(toNumberOrNull("12.5")); // 12.5
console.log(toNumberOrNull(" 12 ")); // 12
console.log(toNumberOrNull("12x")); // null
console.log(toNumberOrNull("")); // 0
