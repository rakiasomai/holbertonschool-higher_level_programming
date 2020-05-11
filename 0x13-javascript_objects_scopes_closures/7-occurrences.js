#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOccur = 0;
  let i = 0;
  for (i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nbOccur++;
    }
  }
  return nbOccur;
};
