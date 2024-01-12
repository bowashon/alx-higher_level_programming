#!/usr/bin/node
const count = process.argv[2];
if (count !== undefined) {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
} else {
  process.exit();
}
