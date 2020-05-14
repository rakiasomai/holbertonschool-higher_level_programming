#!/usr/bin/node
const request = require('request');

const ID = process.argv[2];

request.get('https://swapi-api.hbtn.io/api/films/' + ID, function (err, res, body) {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
