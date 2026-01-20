// S3_OBJ_05 — Invert
function invert(obj) {
  const result = {};

  for (const key in obj) {
    const value = obj[key];

    if (result[value] === undefined) {
      result[value] = key;
    } else if (Array.isArray(result[value])) {
      result[value].push(key);
    } else {
      result[value] = [result[value], key];
    }
  }

  return result;
}

// Tests
console.log(invert({ a: 1, b: 2 }));
// { '1': 'a', '2': 'b' }

console.log(invert({ a: 1, b: 1, c: 2 }));
// { '1': ['a', 'b'], '2': 'c' }
