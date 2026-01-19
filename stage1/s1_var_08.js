function safeAdd(a, b) {
  if (
    typeof a === "number" &&
    typeof b === "number" &&
    Number.isInteger(a) &&
    Number.isInteger(b)
  ) {
    const sum = a + b;

    // If the result is unsafe (or inputs already unsafe), use BigInt
    if (
      !Number.isSafeInteger(a) ||
      !Number.isSafeInteger(b) ||
      !Number.isSafeInteger(sum)
    ) {
      const result = BigInt(a) + BigInt(b);
      console.log("Returned type:", typeof result); // "bigint"
      return result;
    }

    console.log("Returned type:", typeof sum); // "number"
    return sum;
  }

  // Non-integer or non-number: just do normal +
  const result = a + b;
  console.log("Returned type:", typeof result);
  return result;
}

// Tests
safeAdd(10, 20); // number
safeAdd(Number.MAX_SAFE_INTEGER, 1); // bigint
safeAdd(9007199254740993, 1); // bigint
