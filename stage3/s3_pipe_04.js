// S3_PIPE_04 — Array processing pipeline

const pipe =
  (...fns) =>
  (value) =>
    fns.reduce((acc, fn) => fn(acc), value);

// Pipeline steps
const filterValidNumbers = (arr) => arr.filter((x) => !Number.isNaN(+x));

const toNumbers = (arr) => arr.map((x) => +x);

const double = (arr) => arr.map((n) => n * 2);

const sum = (arr) => arr.reduce((a, b) => a + b, 0);

// Build pipeline
const process = pipe(filterValidNumbers, toNumbers, double, sum);

// Test
console.log(process(["1", "2", "x", "3"])); // (1+2+3)*2 = 12
console.log(process(["10", " ", "5"])); // (10+0+5)*2 = 30
