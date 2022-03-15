const fs = require('fs');
let s = fs.readFileSync('./dev/stdin').toString().trim();
let prevLength = s.length;
let count = 0;
let alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='];
for (let a of alphabet) {
    let charSize = a.length;
    count += s.split(a).length - 1;
    s = s.replace(new RegExp(a, 'g'), '0'.repeat(charSize));
}

console.log(s.replace(/0/g, '').length + count);
