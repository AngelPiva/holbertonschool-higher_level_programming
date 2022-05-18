#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

request(url, function (_error, _response, body) {
  console.log(JSON.parse(body).title);
});
