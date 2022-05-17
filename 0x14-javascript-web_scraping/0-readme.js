#!/usr/bin/node

const file = require('fs');

file.readFile(process.argv[2], 'utf-8', function (error, content) {
  if (error) {
    console.log(error);
  } else {
    process.stdout.write(content);
  }
});
