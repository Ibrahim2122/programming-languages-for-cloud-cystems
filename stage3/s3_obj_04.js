// S3_OBJ_04 — Omit
function omit(obj, keys) {
  const result = {};
  const toOmit = new Set(keys);

  for (const key in obj) {
    if (!toOmit.has(key)) {
      result[key] = obj[key];
    }
  }

  return result;
}

// Tests
const user = { id: 1, name: "Ala", role: "admin" };

console.log(omit(user, ["role"]));
// { id: 1, name: "Ala" }

console.log(omit(user, ["id", "name"]));
// { role: "admin" }
