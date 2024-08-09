#!/usr/bin/node
const Square = require('./5-square');
module.exports = class s1 extends Square {
  charPrint (c) {
    if (c) {
      this.c = c;
    } else {
      this.c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(this.c);
      }
      console.log();
    }
  }
};
