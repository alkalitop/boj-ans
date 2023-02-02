const fs = require('fs');
let s = fs.readFileSync('/dev/stdin').toString().trim()

if (s.includes('x')) {
    let tmp = s.split('x');
    let a = Number(tmp[0]), b = Number(tmp[1]);
    let res = '';
    res += Math.abs(a) == 2 ? String(a/2).replace('1', '') : String(a/2);
    res += 'xx';
    if (b) {
        res += b < 0 ? '-' : '+';
        if (Math.abs(b) != 1) res += Math.abs(b);
        res += 'x';
    }
    res += '+W'
    console.log(res)
}
else {
    let b = Number(s);
    let res = '';
    if (b) {
        res += Math.abs(b) == 1 ? String(b).replace('1', '') : String(b);
        res += 'x'
        res += '+'
    }
    res += 'W'
    console.log(res)
}
