#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body).results;
  let index = 0;
  for (const res of body) {
    for (const cha of res.characters) {
      if (cha.includes('18')) {
        index++;
      }
    }
  }
  console.log(index);
});
