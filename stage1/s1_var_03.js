const user = { name: "Ala", tags: [] };

// Mutating the object is allowed
user.tags.push("admin");
user.tags.push("editor");

console.log("Final user object:", user);

// Reassigning the const is NOT allowed
try {
  user = {};
} catch (err) {
  console.log("Error when reassigning const:", err.message);
}
