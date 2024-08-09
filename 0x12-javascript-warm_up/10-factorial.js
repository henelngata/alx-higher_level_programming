#!/usr/bin/node
function factorial (a) {
  if (Number.isNaN(a)) {
    return 1;
  } else if (a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}
const x = factorial(parseInt(process.argv[2]));
console.log(x);
