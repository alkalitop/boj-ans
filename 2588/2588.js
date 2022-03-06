const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let a = input[0]-0, b = input[1]-0;
let t = [
  (b%10), (b%100), (b%1000)
]
console.log(a*t[0]);
console.log(a*(t[1]-t[0])*0.1);
console.log(a*(t[2]-t[1])*0.01);
console.log(a*b);
