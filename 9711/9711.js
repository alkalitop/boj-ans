let seq = [0n, 1n, 1n];
for (let k = 3; k <= 10000; k++) {
    seq[k] = seq[k-1] + seq[k-2];
}

let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let T = input[0];
let testcase = input.slice(1);

for (let i = 0; i < T; i++) {
    let split_cont = testcase[i].trim().split(' ');
    let P = split_cont[0];
    let Q = split_cont[1];
    let M = seq[P] % BigInt(Q)
    console.log(`Case #${i+1}: ${String(M)}`);
}
