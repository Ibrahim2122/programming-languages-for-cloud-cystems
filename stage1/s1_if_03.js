// S1_IF_03 — Truthy / falsy guard
function normalizeName(input) {
  if (!input) {
    return "Anonymous";
  }
  return String(input).trim();
}

// Tests
console.log(normalizeName("")); // "Anonymous"
console.log(normalizeName(" ")); // ""  (truthy string, then trimmed)
console.log(normalizeName(null)); // "Anonymous"
console.log(normalizeName(" Ola ")); // "Ola"
