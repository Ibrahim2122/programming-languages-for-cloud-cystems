// S3_OBJ_06 — Group by
function groupBy(items, key) {
  const result = {};

  for (const item of items) {
    const groupKey = item[key];

    if (result[groupKey] === undefined) {
      result[groupKey] = [];
    }

    result[groupKey].push(item);
  }

  return result;
}

// Tests
const users = [
  { name: "Ala", role: "admin" },
  { name: "Ola", role: "user" },
  { name: "Jan", role: "admin" },
];

console.log(groupBy(users, "role"));
/*
{
  admin: [
    { name: "Ala", role: "admin" },
    { name: "Jan", role: "admin" }
  ],
  user: [
    { name: "Ola", role: "user" }
  ]
}
*/
