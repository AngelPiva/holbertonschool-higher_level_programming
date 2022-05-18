#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (_error, _response, body) {
  const b = JSON.parse(body);
  const dict = {};
  for (let i = 0; i < b.length; i++) {
    const completed = b[i].completed;
    const userId = b[i].userId;
    if (completed === true) {
      if (!(userId in dict)) {
        dict[userId] = 1;
      } else {
        dict[userId] += 1;
      }
    }
  }
  console.log(dict);
});
