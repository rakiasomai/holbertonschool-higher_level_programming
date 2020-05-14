#!/usr/bin/node

const request = require('request');

const movie = process.argv[2];

const givenUrl = `https://swapi-api.hbtn.io/api/films/${movie}`;

request(givenUrl, (err, response, body) => {
  if (!err) {
    const char = JSON.parse(body).characters;
    char.forEach((character) => {
      request(char, function (err, response, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
