const fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().trim().split('\n')
let seq = input[1].trim().split(' ').map(el => el-0);

function isPrime (n) {
    if (n == 1) return 0;
    for (let i = 2; i < n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

let count = 0;
for (let n of seq) {
    count += isPrime(n);
}

console.log(count);
