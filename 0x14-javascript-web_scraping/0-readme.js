#!/usr/bin/node

const fs = require('fs');

fs.readFile(porcess.argv[2], 'utf-8', function(Error, data) {
  if (Error) {
    console.log(Error); 
  }
  else{
    console.log(data);
		        
  }
});
