const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
let M = input[0]-0, N = input[1]-0;

function addPrime (n) {
    if (n == 1) return;
    for (let i = 2; i < n; i++) {
        if (n % i == 0) return;
    }
    if (!minimum) minimum = n;
    psum += n;
}

let primes = [];
let minimum;
let psum = 0;
for (let n = M; n <= N; n++) {
    addPrime(n);
}

if (!minimum) {
    console.log(-1);
}
else {
    console.log(psum);
    console.log(minimum);
}
