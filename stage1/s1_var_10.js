// S1_VAR_10 — Mini debugger
function inspect(value) {
  return {
    type: typeof value,
    isArray: Array.isArray(value),
    isNull: value === null,
    isNaN: Number.isNaN(value),
  };
}

// Explicit tests + output
console.log("null:", inspect(null));
console.log("undefined:", inspect(undefined));
console.log("0:", inspect(0));
console.log("NaN:", inspect(NaN));
console.log('"hello":', inspect("hello"));
console.log("[]:", inspect([]));
console.log("{}:", inspect({}));
console.log(
  "function:",
  inspect(() => {}),
);

// Small asserts
console.assert(
  inspect(null).isNull === true,
  "null should be detected as null",
);
console.assert(
  inspect([]).isArray === true,
  "array should be detected as array",
);
console.assert(inspect(NaN).isNaN === true, "NaN should be detected as NaN");
console.assert(inspect(42).type === "number", "type of 42 should be number");
