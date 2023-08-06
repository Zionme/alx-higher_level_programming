#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body).characters;
  printCharacters(data, 0);
});

function printCharacters (data, index) {
  request.get(data[index], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < data.length) {
        printCharacters(data, index + 1);
      }
    }
  });
}
