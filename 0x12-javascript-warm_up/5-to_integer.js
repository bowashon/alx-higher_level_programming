#!/usr/bin/node
const firstarg = process.argv[2];
if (firstarg !== undefined) {
  const integerValue = parseInt(firstarg);
  if (!isNaN(integerValue)) {
    console.log('My number: ' + integerValue);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
