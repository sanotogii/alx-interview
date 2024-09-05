#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function getCharacters () {
  request(movieUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie details:', error.message);
      return;
    }

    const characterUrls = body.characters;
    let completedRequests = 0;

    characterUrls.forEach((characterUrl) => {
      request(characterUrl, { json: true }, (error, response, character) => {
        if (error) {
          console.error('Error fetching character details:', error.message);
        } else {
          console.log(character.name);
        }

        completedRequests++;
        if (completedRequests === characterUrls.length) {
          process.exit(0);
        }
      });
    });
  });
}

getCharacters();
