#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      print(){
        const x = 'X';
	for (let i=0; i < w; i++){
	  console.log(x);
          for (let y=i; y < h; y++){
            console.log(x);
          }
        }

      }
    }
  }
}
module.exports = Rectangle;
