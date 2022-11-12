let A = require('fs').readFileSync('/dev/stdin').toString().split('\n')[1].trim().split(' ');
let res = A.sort((a, b) => Number(a+b)-Number(b+a)).reverse().join('');
if (res.replace(/0/g, '') == '') {
    console.log('0');
}
else {
    console.log(res);
}
