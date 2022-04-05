stdin=require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');input=_=>(stdin.splice(0, 1)+'').trim();

input();
let A = BigInt(input()), B = BigInt(input());
console.log(String(A*B))
