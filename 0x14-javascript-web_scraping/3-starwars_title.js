#!/usr/bin/node
const request = require('request');
const urlpath = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(urlpath, 'utf-8', function (err, data) {
  if (err) throw err;
  data = JSON.parse(data.body);
  const title = data.title;
  console.log(title);
});
