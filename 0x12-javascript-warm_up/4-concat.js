#!/usr/bin/node

let A = 'undefined';
let B = 'undefined';
if (process.argv[2]) {
  A = process.argv[2];
}
if (process.argv[3]) {
  B = process.argv[3];
}
console.log(A + ' is ' + B);
