const fs = require('fs');

let y = fs.readFileSync('/dev/stdin').toString();
console.log(y - 543);
