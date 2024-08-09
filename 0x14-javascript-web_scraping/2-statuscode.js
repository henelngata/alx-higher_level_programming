#!/usr/bin/node
const req = require('request');
const uri = process.argv[2];
req.get(uri, function (err, data) {
  if (err) throw err;
  console.log(`code: ${data.statusCode}`);
});
