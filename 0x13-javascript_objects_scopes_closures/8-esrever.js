#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  const reverseList = [];
  while (i < list.length) {
    reverseList.unshift(list[i]);
    i++;
  }
  return reverseList;
};
