#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((num, current) => current === searchElement ? num + 1 : num, 0);
};
