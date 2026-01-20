// S3_PIPE_01 — pipe()
function pipe(...fns) {
  return function (value) {
    return fns.reduce((acc, fn) => fn(acc), value);
  };
}

// Tests
const add1 = (x) => x + 1;
const double = (x) => x * 2;
const square = (x) => x * x;

const run = pipe(add1, double, square);
console.log(run(2)); // ((2 + 1) * 2)² = 36
