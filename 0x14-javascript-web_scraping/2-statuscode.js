#!/usr/bin/node

const request = require('request');

const takeUrl = process.argv[2] || '';

request(takeUrl, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  console.log('code: ' + response.statusCode);
});
