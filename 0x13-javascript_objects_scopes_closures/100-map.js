#!/usr/bin/node
let list = require('./100-data').list;
console.log(list);
list = list.map((x, y) => {
  return x * y;
});
console.log(list);
