#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (_error, _response, body) {
  const results = JSON.parse(body).results;
  let count = 0;
  for (let cs = 0; cs < results.length; cs++) {
    const characters = results[cs].characters;
    for (let c = 0; c < characters.length; c++) {
      if (characters[c].split('/')[5] === '18') {
        count += 1;
      }
    }
  }
  console.log(count);
});
