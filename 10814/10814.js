let members = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').slice(1);
members.sort((a, b) => {
    let ageA = a.split(' ')[0];
    let ageB = b.split(' ')[0];
    return ageA - ageB;
});
members.forEach(el => {
    console.log(el);
});
