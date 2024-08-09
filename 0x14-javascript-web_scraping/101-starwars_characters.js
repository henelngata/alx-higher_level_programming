#!/usr/bin/node
const request = require('request');

// Build the URL using the movie ID passed as an argument
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Fetch movie details and start printing characters
request(url, function (error, response, body) {
  if (error) {
    console.error('Error fetching movie details:', error);
    return;
  }

  const characters = JSON.parse(body).characters;
  if (characters.length > 0) {
    printCharacters(characters, 0);
  }
});

// Recursive function to print characters in order
function printCharacters (characters, index) {
  if (index >= characters.length) return;

  request(characters[index], function (error, response, body) {
    if (error) {
      console.error('Error fetching character details:', error);
      return;
    }

    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}
