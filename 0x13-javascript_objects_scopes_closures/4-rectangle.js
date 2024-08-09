#!/usr/bin/node
/*
Write a class Rectangle that defines a rectangle:
 */
module.exports = class Rectangle {
  // The constructor must take 2 arguments w and h
  // If w or h is equal to 0 or not a positive integer,create an empty object
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  // instance method prints the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  // that exchanges the width and the height of the rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  //  multiples the width and the height of the rectangle by 2
  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
