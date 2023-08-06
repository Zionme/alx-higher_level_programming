#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
const url = process.argv[2];
const request = require('request');

request.get(url, function (err, res, body) {
  if (!err) {
    const data = JSON.parse(body);
    const tasks = {};
    data.forEach((d) => {
      if (d.completed && tasks[d.userId] === undefined) {
        tasks[d.userId] = 1;
      } else if (d.completed) {
        tasks[d.userId] += 1;
      }
    });
    console.log(tasks);
  }
});
