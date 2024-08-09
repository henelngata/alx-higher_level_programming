#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf-8', function (errors, data) {
  if (errors) throw errors;
  console.log(data);
});
