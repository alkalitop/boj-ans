stdin=require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');input=_=>(stdin.splice(0, 1)+'').trim();

let tmp = input().split(' ').map(el => BigInt(el));
console.log(String(tmp[0]*tmp[1]))
