const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let X = input[0].trim().split(' ')[1];
let A = input[1].trim().split(' ');
console.log(A.filter(el => el-0 < X).join(' '));
