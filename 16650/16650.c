#include<stdio.h>
int m = 998244353;
int dp[200001][448];

int P(int n, int k) {
    if (n == 0 && k == 0) {
        return 1;
    }
    if ((n <= 0 || k <= 0) || n < k) {
        return 0;
    }
    
    int t = dp[n][k];
    if (!t) {
        dp[n][k] = P(n-k, k) + P(n-1, k-1);
        dp[n][k] = dp[n][k] % m;
        return dp[n][k];
    }
    else {
        return t;
    }
}
        
int Q(int n) {
    int r = 0;
    for (int i = ((n & 1) ? 1 : 2); i*i <= n; i += 2) {
        r += P(i + ((n-i*i) >> 1), i);
        r = r % m;
    }
    return r;
}

int main(void) {
    int s;
    scanf("%d ", &s);
    
    for (int i = 0; i < s; i++) {
        int n;
        scanf("%d ", &n);
        printf("%d\n", Q(n));
    }
    return 0;
}

