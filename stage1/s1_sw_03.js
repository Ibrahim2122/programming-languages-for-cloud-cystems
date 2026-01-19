// S1_SW_03 — Simple calculator
function calc(a, op, b) {
  switch (op) {
    case "+":
      return a + b;
    case "-":
      return a - b;
    case "*":
      return a * b;
    case "/":
      if (b === 0) return null;
      return a / b;
    default:
      return null;
  }
}

// Tests
console.log(calc(4, "+", 2)); // 6
console.log(calc(4, "-", 2)); // 2
console.log(calc(4, "*", 2)); // 8
console.log(calc(4, "/", 2)); // 2
console.log(calc(4, "/", 0)); // null
console.log(calc(4, "%", 2)); // null
