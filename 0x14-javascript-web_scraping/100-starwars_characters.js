#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body);
  for (const name of body.characters) {
    request(name, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const data = JSON.parse(body).name;
      console.log(data);
    });
  }
});
