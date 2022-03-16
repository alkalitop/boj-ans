const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
let A = input[0], B = input[1], Z = input[2];
console.log(Math.ceil((Z-A)/(A-B))+1);
