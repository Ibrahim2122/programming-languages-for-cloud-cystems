// S2_ARR_06 — Transform records
function activeUserNames(users) {
  return users
    .filter((u) => u.active)
    .map((u) => u.name.toUpperCase())
    .sort();
}

// Tests
const users = [
  { id: 1, name: "ala", active: true },
  { id: 2, name: "ola", active: false },
  { id: 3, name: "jan", active: true },
];

console.log(activeUserNames(users)); // ["ALA", "JAN"]
