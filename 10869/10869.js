const fs = require('fs');

let z = fs.readFileSync('/dev/stdin').toString().split(' ');
console.log((z[0]-0) + (z[1]-0));
console.log(z[0] - z[1]);
console.log((z[0]-0) * (z[1]-0));
console.log((z[0]-0) / (z[1]-0) | 0);
console.log((z[0]-0) % (z[1]-0));
