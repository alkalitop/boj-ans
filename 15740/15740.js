let z = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');
let A = BigInt(z[0]), B = BigInt(z[1]);
console.log(String(A + B))
