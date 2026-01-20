// S3_OBJ_03 — Pick
function pick(obj, keys) {
  const result = {};

  for (const key of keys) {
    if (key in obj) {
      result[key] = obj[key];
    }
  }

  return result;
}

// Tests
const user = { id: 1, name: "Ala", role: "admin" };

console.log(pick(user, ["id", "name"]));
// { id: 1, name: "Ala" }

console.log(pick(user, ["role", "email"]));
// { role: "admin" }
