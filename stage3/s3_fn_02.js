// S3_FN_02 — Sort by property
const people = [
  { name: "Ala", age: 30 },
  { name: "Ola", age: 20 },
  { name: "Jan", age: 25 },
];

people.sort((a, b) => a.age - b.age);

// Test
console.log(people);
// [
//   { name: "Ola", age: 20 },
//   { name: "Jan", age: 25 },
//   { name: "Ala", age: 30 }
// ]
