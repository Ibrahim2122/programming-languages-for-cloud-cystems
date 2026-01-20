// S3_PIPE_02 — compose()
function compose(...fns) {
  return function (value) {
    return fns.reduceRight((acc, fn) => fn(acc), value);
  };
}

// Tests
const add1 = (x) => x + 1;
const double = (x) => x * 2;
const square = (x) => x * x;

const run = compose(square, double, add1);
console.log(run(2)); // square(double(add1(2))) = 36
