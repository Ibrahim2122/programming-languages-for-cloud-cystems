// S3_PIPE_03 — String normalization pipeline

const trim = (s) => s.trim();
const toLower = (s) => s.toLowerCase();
const normalizeSpaces = (s) => s.replace(/\s+/g, " ");

function pipe(...fns) {
  return (value) => fns.reduce((acc, fn) => fn(acc), value);
}

const normalizeString = pipe(trim, toLower, normalizeSpaces);

// Test
console.log(normalizeString("  HeLLo   WoRLD   ")); // "hello world"
