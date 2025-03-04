#include <iostream>
using namespace std;
typedef long long ll;

typedef struct {
    ll raw[2][2];
} Matrix;

const ll m = 1000000007;

Matrix matmul(const Matrix& A, const Matrix& B, const ll p) {
    ll C00 = (((A.raw[0][0] * B.raw[0][0] + p) % p) + ((A.raw[0][1] * B.raw[1][0] + p) % p)) % p;
    ll C01 = (((A.raw[0][0] * B.raw[0][1] + p) % p) + ((A.raw[0][1] * B.raw[1][1] + p) % p)) % p;
    ll C10 = (((A.raw[1][0] * B.raw[0][0] + p) % p) + ((A.raw[1][1] * B.raw[1][0] + p) % p)) % p;
    ll C11 = (((A.raw[1][0] * B.raw[0][1] + p) % p) + ((A.raw[1][1] * B.raw[1][1] + p) % p)) % p;
    return { {{C00, C01}, {C10, C11}} };
}

Matrix matexp(Matrix& A, int exp, ll p) {
    Matrix ret = { {{1, 0}, {0, 1}} };
    while (exp) {
        if (exp & 1) ret = matmul(A, ret, p);
        exp >>= 1; A = matmul(A, A, p);
    }
    return ret;
}

int ipow(ll x, ll y, ll p) {
    if (!y) {
        return 1;
    }
    else if (y == 1) {
        return x % p;
    }
    else {
        ll t = ipow(x, y >> 1, p);
        return (y & 1 ? (t * t % p) * x : t * t) % p;
    }
}

Matrix calc(ll n) {
    if (!n) {
        ll t = ipow(4 * m - 5, m - 2, m);
        return {
            { { m - t, (t * (m - 1) + m) % m }, { (4 * t + m) % m, m - t } }
        };
    }
    Matrix A = { 
        { {1, m - 1}, {4, 1} }
    };
    return matexp(A, n - 1, m);
}

ll extr(Matrix A) {
    return A.raw[1][1] - A.raw[1][0];
}

ll query(ll i, ll j, ll k) {
    ll w = ipow(5, k, m);
    Matrix A = {
        {{1, m - 1}, {4, 1}}
    };
    Matrix s0 = calc(k);
    Matrix s1 = calc(k * (i - 1));
    Matrix s2 = calc(k * j);
    ll c1 = (extr(s2) - extr(s1) + m) % m;
    Matrix s10 = matmul(matmul(s0, s1, m), A, m);
    Matrix s20 = matmul(matmul(s0, s2, m), A, m);
    ll c2 = (extr(s20) - extr(s10) + m) % m;
    ll upper = (w * c1 - c2 + m) % m;
    ll lower = (w - 2 * extr(s0) + 1 + m) % m;
    return upper * ipow(lower, m - 2, m) % m;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ll Q, i, j, k;
    cin >> Q;
    for (int q = 0; q < Q; q++) {
        cin >> i >> j >> k;
        cout << (query(i, j, k) + m) % m << "\n";
    }
    return 0;
}
