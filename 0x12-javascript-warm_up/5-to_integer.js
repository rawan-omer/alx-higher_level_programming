#!/usr/bin/node
// prints My number: <first argument converted in integer>

if (isNaN(process.argv[2])) {
  console.log("Not a numbe");
} else {
  console.log("My number: " + parseInt(process.argv[2]));
}
