const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(el => el.trim());

let tc = input[0];
let strs = input.slice(1);
let count = 0;
for (s of strs) {
    let cs = new Set();
    let comp = 1;
    for (let i = 0; i < s.length; i++) {
        if (cs.has(s[i])) {
            if (s[i-1] !== s[i]) {
                comp = 0;
                break;
            }
        }
        cs.add(s[i]);
    }
    count += comp;
}

console.log(count);
