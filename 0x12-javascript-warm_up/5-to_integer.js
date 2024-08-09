#!/usr/bin/node
//  script that prints

const str = process.argv[2];
if (str) {
  if (parseInt(str)) {
    const num = parseInt(str);
    console.log('My number: ' + num);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
