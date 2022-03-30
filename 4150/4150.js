let prev = [0n, 1n, 1n]

function f (k) {
    if (!prev[k]) {
        prev[k] = f(k-1) + f(k-2);
    }
    return prev[k];
}

let N = require('fs').readFileSync('/dev/stdin').toString().trim()-0;
console.log(String(f(N)));
