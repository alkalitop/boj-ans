let X = require('fs').readFileSync('/dev/stdin').toString().trim()
let count = 0;
while ((X-0) > 9) {
    X = String(X.split('').reduce(function (a, b) {
        return BigInt(a) + BigInt(b);
    }))
    count++;
}
console.log(count);
if ((X-0) % 3) {
    console.log('NO');
}
else {
    console.log('YES');
}
