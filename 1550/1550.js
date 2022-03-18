const fs = require('fs');
console.log(parseInt(fs.readFileSync('/dev/stdin').toString().trim(), 16))
