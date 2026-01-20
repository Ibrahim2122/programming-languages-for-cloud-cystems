// S3_OBJ_01 — Safe read
function get(obj, path, fallback) {
  const parts = path.split(".");
  let current = obj;

  for (const key of parts) {
    if (current == null || !(key in current)) {
      return fallback;
    }
    current = current[key];
  }

  return current;
}

// Tests
const data = {
  a: {
    b: {
      c: 42,
    },
  },
};

console.log(get(data, "a.b.c", null)); // 42
console.log(get(data, "a.b.x", "N/A")); // "N/A"
console.log(get(data, "a.x.c", "N/A")); // "N/A"
console.log(get(data, "a.b", null)); // { c: 42 }
