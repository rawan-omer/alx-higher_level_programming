#!/usr/bin/node
// adding two argument

function add (a, n) {
  return parseInt(a) + parseInt(n);
}

console.log(add(process.argv[2], process.argv[3]));
