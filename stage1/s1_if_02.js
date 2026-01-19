// S1_IF_02 — Score to grade
function grade(score) {
  if (typeof score !== "number" || score < 0 || score > 100) {
    return null;
  }

  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
}

// Tests
console.log(grade(95)); // "A"
console.log(grade(82)); // "B"
console.log(grade(74)); // "C"
console.log(grade(61)); // "D"
console.log(grade(40)); // "F"
console.log(grade(-5)); // null
console.log(grade(120)); // null
