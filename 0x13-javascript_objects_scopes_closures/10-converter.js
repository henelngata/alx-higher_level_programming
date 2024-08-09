#!/usr/bin/node
exports.converter = function (base) {
  return bse => bse.toString(base);
};
