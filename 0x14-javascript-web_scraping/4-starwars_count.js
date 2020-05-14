#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    let count = 0;
    const movies = JSON.parse(body).results;
    for (const num of movies) {
      for (const str of num.characters) {
        if (str.endsWith('18/')) { count++; }
      }
    }
    console.log(count);
  }
});
