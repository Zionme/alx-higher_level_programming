#!/usr/bin/node
//  a script that prints the title of a Star Wars movie where
//  the episode number matches a given integer.
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
request.get(url, function (err, response, body) {
  if (!err) {
    console.log(JSON.parse(body).title);
  }
});
