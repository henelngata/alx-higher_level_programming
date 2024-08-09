#!/usr/bin/node
const request = require('request');
const ts = require('fs');
const urlpath = process.argv[2];
request.get(urlpath, 'utf-8', function (err, data) {
  if (err) throw err;
  ts.writeFile(process.argv[3], data.body, 'utf-8', function (err) {
    if (err) throw err;
  });
});
