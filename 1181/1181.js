const fs = require('fs');
let words = Array.from(new Set(fs.readFileSync('/dev/stdin').toString().trim().replace(/\s*\n/g, '\n').split('\n').slice(1)))
words.sort((a, b) => {
    if (a.length == b.length) {
        if (a > b) return 1;
        if (a < b) return -1;
    }
    else {
        return a.length - b.length;
    }
});
for (let v of words) {
    console.log(v);
}
