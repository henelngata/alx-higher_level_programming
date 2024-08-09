#!/usr/bin/node

if (process.argv && parseInt(process.argv[2])) {
  const num = process.argv[2];
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
