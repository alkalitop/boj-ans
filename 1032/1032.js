const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(el => el.trim()).slice(1);
let tab = [];
for (let s of input) {
    for (let i in s) {
        if (tab[i]) continue;
        if (input[0][i] != s[i]) tab[i] = 1;
    }
}
console.log(input[0].split('').map((el, i) => {
    if (tab[i]) {
        return '?'
    }
    else return el;
}).join(''))
