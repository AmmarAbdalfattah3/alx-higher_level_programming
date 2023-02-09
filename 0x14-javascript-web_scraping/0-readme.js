#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function(Error, data) {
  if (Error) {
    console.log(Error); 
  }
  console.log(data);
});
