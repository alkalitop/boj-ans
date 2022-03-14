const fs = require('fs');
let s = fs.readFileSync('/dev/stdin').toString().trim().toUpperCase();

let freq = {}
for (let i = 0; i < s.length; i++) {
    let cur = s[i];
    if (!freq[cur]) freq[cur] = 0;
    freq[cur]++;
}
let max = Math.max.apply(null, Object.values(freq));
let mostfreq = Object.keys(freq).filter(el => freq[el] === max);
if (mostfreq.length === 1) {
    console.log(mostfreq[0]);
}
else {
    console.log('?');
}
