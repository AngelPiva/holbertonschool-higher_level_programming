#!/usr/bin/node

const request = require('request');

request.Readfile (process.argv[2], 'utf-8', function (error, content) {
 if (error) {
  console.log(error);
 } else {
  console.log(content);
 }
});