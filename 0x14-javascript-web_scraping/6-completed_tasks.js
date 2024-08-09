#!/usr/bin/node
//  computes the number of tasks completed by user id.

const request = require('request');
const urlpath = process.argv[2];
request.get(urlpath, 'utf-8', function (err, data) {
  if (err) throw err;
  data = JSON.parse(data.body);
  const obj = {};
  for (let i = 0; i < data.length; i++) {
    const element = data[i];
    const id = element.userId;
    const complete = element.completed;
    if (obj[id] && complete === true) {
      obj[id] = obj[id] + 1;
    } else if (!obj[id] && complete === true) {
      obj[id] = 1;
    }
  }
  console.log(obj);
});
