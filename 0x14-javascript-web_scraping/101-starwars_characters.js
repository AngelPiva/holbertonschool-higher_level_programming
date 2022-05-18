#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

request(url, function (_error, _response, body) {
  const chars = JSON.parse(body).characters;
  for (let cs = 0; cs < chars.length; cs++) {
    request(chars[cs], function (_err, _resp, bod) {
      const name = JSON.parse(bod).name;
      console.log(name);
    });
  }
});
