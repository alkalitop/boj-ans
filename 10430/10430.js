const fs = require('fs');
let z = fs.readFileSync('/dev/stdin').toString().split(' ');

let a = z[0]-0, b = z[1]-0, c = z[2]-0;
console.log((a+b)%c);
console.log(((a%c)+(b%c))%c);
console.log((a*b)%c);
console.log(((a%c)*(b%c))%c);
