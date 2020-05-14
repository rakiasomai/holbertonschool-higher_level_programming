#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const URL = process.argv[2] || '';
const Path = process.argv[3];

request(URL, (err, response, body) => {
  if (err) {
    return console.log(err);
  }

  fs.writeFile(Path, body, 'utf8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
