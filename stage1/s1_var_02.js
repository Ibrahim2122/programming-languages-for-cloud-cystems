// 1) Using let
{
  let x = 10;
}

try {
  console.log(x);
} catch (err) {
  console.log(
    "Oops! 'x' was declared with let and is not accessible outside its block.",
  );
}

// 2) Using var
{
  var y = 20;
}

try {
  console.log(y);
} catch (err) {
  console.log("This will not run.");
}
