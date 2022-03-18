const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let A = BigInt(input[0]), B = BigInt(input[1]);
console.log(String(A + B));
console.log(String(A - B));
console.log(String(A * B));
