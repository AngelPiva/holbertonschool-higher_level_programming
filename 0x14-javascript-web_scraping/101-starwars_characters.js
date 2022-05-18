#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const axios = require('axios');

async function printchars () {
  const response = await axios.get(url);
  const chars = response.data.characters;
  for (let c = 0; c < chars.length; c++) {
    const ch = chars[c];
    await axios.get(ch)
      .then(function (person) {
        console.log(person.data.name);
      });
  }
}

printchars();
