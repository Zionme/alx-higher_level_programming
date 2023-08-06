#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.
const url = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('fs');

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
