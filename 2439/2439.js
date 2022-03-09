const fs = require('fs');
let N = fs.readFileSync('/dev/stdin').toString()-0;
for (let i = N-1; i >= 0; i--) {
    console.log(' '.repeat(i) + '*'.repeat(N-i));
}
