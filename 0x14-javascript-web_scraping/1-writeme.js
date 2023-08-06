#!/usr/bin/node
// a script that writes a string to a file.
const fileName = process.argv[2];
const data = process.argv[3];
const fs = require('fs');

fs.writeFile(fileName, data, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
