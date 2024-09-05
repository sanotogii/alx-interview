#!/usr/bin/node

const request = require('request-promise');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

async function getCharacters () {
  try {
    const movieResponse = await request({ uri: movieUrl, json: true });

    for (const characterUrl of movieResponse.characters) {
      const characterResponse = await request({ uri: characterUrl, json: true });
      console.log(characterResponse.name);
    }
  } catch (error) {
    console.error('Error fetching details:', error.message);
  }
}

getCharacters();
