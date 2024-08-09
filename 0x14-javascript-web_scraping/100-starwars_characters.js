#!/usr/bin/node
//  computes the number of tasks completed by user id.

const request = require('request');
const urlpath = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(urlpath, 'utf-8', function (err, data) {
  if (err) throw err;
  data = JSON.parse(data.body);
  const character = data.characters;
  for (let i = 0; i < character.length; i++) {
    const element = character[i];
    request.get(element, 'utf-8', function (err, char) {
      if (err) throw err;
      char = JSON.parse(char.body);
      console.log(char.name);
    });
  }
});
