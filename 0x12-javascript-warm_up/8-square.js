#!/usr/bin/node
const i = process.argv[2];

if (i !== undefined) {
  if (!isNaN(parseInt(i))) {
    for (let a = 0; a < i; a++) {
      let row = '';
      for (let b = 0; b < i; b++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log('Missing size');
  }
} else {
  process.exit();
}
