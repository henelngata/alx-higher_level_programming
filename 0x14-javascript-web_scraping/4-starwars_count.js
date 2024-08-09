#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Status code', response.statusCode);
    return;
  }

  const movies = JSON.parse(body).results;
  let wedgeMovieCount = 0;

  for (const movie of movies) {
    const characters = movie.characters;
    for (const characterUrl of characters) {
      if (characterUrl.includes('/18/')) { // Wedge Antilles has ID 18
        wedgeMovieCount++;
        break; // No need to check other characters in the same movie
      }
    }
  }

  console.log(wedgeMovieCount);
});
