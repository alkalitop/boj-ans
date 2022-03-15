const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim();

let keymap = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'];
let t = 0;
for (let i = 0; i < input.length; i++) {
    t += keymap.findIndex(el => el.includes(input[i])) + 1
}
console.log(t);
