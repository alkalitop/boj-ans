let seq = [0n, 1n, 1n];
for (let k = 3; k <= 10000; k++) {
    seq[k] = seq[k-1] + seq[k-2];
}

let N = require('fs').readFileSync('/dev/stdin').toString()-0;
console.log(String(seq[N]))
