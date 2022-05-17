#!/usr/bin/node

const file = require('file');

file.Readfile (process.argv[2], 'utf-8', function (error, content) {
 if (error) {
  console.log(error);
 } else {
  console.log(content);
 }
});