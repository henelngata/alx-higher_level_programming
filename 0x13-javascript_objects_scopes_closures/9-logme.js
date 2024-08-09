#!/usr/bin/node
let itemPrinted = 0;
exports.logMe = function (item) {
  console.log(`${itemPrinted++}: ${item}`);
};
