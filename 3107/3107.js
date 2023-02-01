const fs = require('fs');

let s = fs.readFileSync('/dev/stdin').toString().trim();
if (s.includes('::')) {
    s = s.replace('::', ':0'.repeat(8 - s.replace('::', ':').split(':').length) + ':')
}
s = s.split(':').map(el => el.padStart(4, '0')).join(':')
console.log(s)
