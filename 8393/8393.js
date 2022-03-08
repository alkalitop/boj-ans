const fs = require('fs');
let n = fs.readFileSync('/dev/stdin').toString()-0;
console.log(n*(n+1)/2);
