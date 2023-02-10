#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const completed = {};
  const todos = JSON.parse(body);
  for (const todo of todos) {
    if (!completed[todo.userId]) {
      completed[todo.userId] = 0;
    }
    if (todo.completed === true) {
      completed[todo.userId] += 1;
    }
  }
  console.log(completed);
});
