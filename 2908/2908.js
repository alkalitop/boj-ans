const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim()
let z = input.split(' ');
console.log(Math.max(z[0].split('').reverse().join('')-0, z[1].split('').reverse().join('')-0));
