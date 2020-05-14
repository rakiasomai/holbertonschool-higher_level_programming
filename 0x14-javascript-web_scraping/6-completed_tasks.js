#!/usr/bin/node
const url = process.argv[2];

const request = require('request');

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  if (res.statusCode === 200) {
    const base = JSON.parse(body);
    const dcte = {};

    for (const task of base) {
      if (task.completed === true) {
        if (task.userId in dcte) {
          dcte[task.userId] += 1;
        } else {
          dcte[task.userId] = 1;
        }
      }
    }
    console.log(dcte);
  }
});
