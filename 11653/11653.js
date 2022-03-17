const fs = require('fs');
let n = fs.readFileSync('/dev/stdin').toString().trim()-0;

function factorize (n) {
    if (n == 1) return null;
    let primes = [];
    let div = 2;
    while (n > 1) {
        if (n % div === 0) {
            primes.push(div);
            n /= div;
        }
        else {
            div++;
        }
    }
    return primes;
}

let result = factorize(n);
if (result) {
    for (let z of result) console.log(z);
}
