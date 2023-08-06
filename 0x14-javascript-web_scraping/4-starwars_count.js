#!/usr/bin/node
// a script that prints the number of movies where the
// character “Wedge Antilles” is present.
const url = process.argv[2];
const request = require('request');
let count = 0;
request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body);
    for (let i = 0; films.results[i] !== undefined; i++) {
      const characters = films.results[i].characters;
      for (let j = 0; characters[j] !== undefined; j++) {
        const m = characters[j].split('/');
        if (m.includes('18')) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
