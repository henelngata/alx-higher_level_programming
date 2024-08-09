#!/usr/bin/node

let Second = 0;
const newArr = [];
if (process.argv[2]) {
  if (process.argv.length <= 3) {
    console.log('0');
  } else {
    const array = process.argv;
    for (let index = 2; index < array.length; index++) {
      newArr.push(array[index]);
    }
    newArr.sort(function (a, b) { return a - b; });
    Second = newArr[newArr.length - 2];
    console.log(Second);
  }
} else {
  console.log('0');
}
