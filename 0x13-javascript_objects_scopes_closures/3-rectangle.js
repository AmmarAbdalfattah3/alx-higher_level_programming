#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = function () {
      const x = 'X';
      for (let i = 0; i < h; i++) {
        console.log(x.repeat(w));
      }
    };
  }
}
module.exports = Rectangle;
