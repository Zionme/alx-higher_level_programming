#!/usr/bin/node
// a script that reads and prints the content of a file.
const fileName = process.argv[2];
const fs = require('fs');

fs.readFile(fileName, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
