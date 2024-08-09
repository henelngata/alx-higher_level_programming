#!/usr/bin/node
const request = require('request');
urlpath = process.argv[2];
request.get('https://swapi-api.alx-tools.com/api/films', 'utf-8', function (err, data) {
  if (err) throw err;
  data = JSON.parse(data.body);
  const results = data.results;
  for (let i = 0; i < results.length; i++) {
    const characters = results[i].characters;
    for (let k = 0; k < characters.length; k++) {
      const chatacter = characters[k];
      request.get(chatacter, function (err, data) {
        if (err) throw err;
        const jsondata = JSON.parse(data.body);
        if (jsondata.name === 'Wedge Antilles') {
          const len = jsondata.films;
          console.log(len);
        }
      });
    }
  }
});
