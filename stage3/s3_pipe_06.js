// S3_PIPE_06 — Safe pipeline
function pipeSafe(...fns) {
  return function (value) {
    try {
      const result = fns.reduce((acc, fn) => fn(acc), value);
      return { ok: true, value: result };
    } catch (error) {
      return { ok: false, error };
    }
  };
}

// Tests
const parseNumber = (x) => {
  const n = Number(x);
  if (Number.isNaN(n)) throw new Error("Not a number");
  return n;
};

const double = (x) => x * 2;

const safeProcess = pipeSafe(parseNumber, double);

console.log(safeProcess("10"));
// { ok: true, value: 20 }

console.log(safeProcess("abc"));
// { ok: false, error: Error: Not a number }
