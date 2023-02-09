#!/usr/bin/node

const fs = require('fs');

var file_arguments = process.argv[2];

fs.readFile(file_arguments, 'utf-8', function(Error, data) {
  if (Error) {
    console.log(Error); 
  }
  else{
    console.log(data);
		        
  }
})
