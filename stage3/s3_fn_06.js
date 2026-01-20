// S3_FN_06 — Map values
function mapValues(obj, fn) {
  const result = {};

  for (const key in obj) {
    result[key] = fn(obj[key], key);
  }

  return result;
}

// Tests
const data = { a: 1, b: 2, c: 3 };

const doubled = mapValues(data, (v) => v * 2);
console.log(doubled);
// { a: 2, b: 4, c: 6 }
