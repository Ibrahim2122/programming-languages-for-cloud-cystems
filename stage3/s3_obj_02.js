// S3_OBJ_02 — Merge config
function mergeDefaults(defaults, overrides) {
  return {
    ...defaults,
    ...overrides,
  };
}

// Tests
const defaults = {
  host: "localhost",
  port: 3000,
  debug: false,
};

const overrides = {
  port: 8080,
  debug: true,
};

const result = mergeDefaults(defaults, overrides);

console.log(result);
// { host: 'localhost', port: 8080, debug: true }

// Verify inputs not mutated
console.log(defaults);
// { host: 'localhost', port: 3000, debug: false }
console.log(overrides);
// { port: 8080, debug: true }
