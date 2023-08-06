#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (let i = 0; data.characters[i] !== undefined; i++) {
    request.get(data.characters[i], function (err, res, body) {
      if (err) {
        console.log(err);
      } else {
        console.log(JSON.parse(body).name);
      }
    });
  }
});
