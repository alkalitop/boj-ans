const input = require('fs').readFileSync('/dev/stdin').toString().split('\n')

let dp = {}
let w = function (a, b, c) {
    if (!dp[a]) dp[a] = {}
    if (!dp[a][b]) dp[a][b] = {}
    if (!dp[a][b-1]) dp[a][b-1] = {}
    if (!dp[a-1]) dp[a-1] = {}
    if (!dp[a-1][b]) dp[a-1][b] = {}
    if (!dp[a-1][b-1]) dp[a-1][b-1] = {}
    if (a <= 0 || b <= 0 || c <= 0) {
        return 1;
    }
    else if (a > 20 || b > 20 || c > 20) {
        return w(20, 20, 20);
    }
    else if (a < b && b < c) {
        if (!dp[a][b][c]) dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c);
        return dp[a][b][c];
    }
    else {
        if (!dp[a][b][c]) dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);
        return dp[a][b][c];
    }
}

for (let s of input) {
    let p = s.trim().split(' ');
    let a = Number(p[0]), b = Number(p[1]), c = Number(p[2]);
    if (a == -1 && b == -1 && c == -1) break;
    console.log(`w(${a}, ${b}, ${c}) = ${w(a, b, c)}`);
}
