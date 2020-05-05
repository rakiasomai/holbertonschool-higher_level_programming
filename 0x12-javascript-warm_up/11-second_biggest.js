#!/usr/bin/node
let args = 0;
const m = process.argv.slice(2);
if (m.length > 1) {
  m.sort((x, y) => x - y);
  args = m[m.length - 2];
}
console.log(args);
