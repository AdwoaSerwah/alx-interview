#!/usr/bin/node

const request = require('request'); // Import the request module

// Function to make a request and return a Promise
const getCharacterName = url => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error); // Reject if there's an error
      } else {
        const character = JSON.parse(body);
        resolve(character.name); // Resolve with the character's name
      }
    });
  });
};

// Get the movie ID from command line argument
const movieId = process.argv[2];

// Check if the movie ID is provided
if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

// Construct the URL to access the specific movie
const url = `https://swapi.dev/api/films/${movieId}/`;

// Send a GET request to the Star Wars API
request(url, async (error, response, body) => {
  if (error) {
    console.log('Error:', error); // Handle any errors during the request
    process.exit(1);
  }

  // Check if the response body is a valid JSON object
  try {
    const movie = JSON.parse(body); // Parse the JSON response

    if (!movie.characters) {
      console.log('No characters found for this movie.');
      return;
    }

    const characters = movie.characters; // Extract the characters list

    // Use async/await to ensure characters are printed in order
    const characterPromises = characters.map(characterUrl => getCharacterName(characterUrl));
    const characterNames = await Promise.all(characterPromises);

    // Print the character names in order
    characterNames.forEach(name => console.log(name));
  } catch (e) {
    console.log('Error parsing the response:', e);
  }
});
