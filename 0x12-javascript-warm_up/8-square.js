#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let n = 0; n < parseInt(process.argv[2]); n++) {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else console.log('Missing size');
