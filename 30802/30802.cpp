#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n;
    vector<int> v;
    int t, p;
    cin >> n;
    int u;
    for (int i = 0; i < 6; i++) {
        cin >> u;
        v.push_back(u);
    }
    cin >> t >> p;
    int r = 0;
    for (int i = 0; i < 6; i++) {
        r += (v[i] + t-1) / t;
    }
    cout << r << endl;
    cout << n/p << ' ' << n%p;
    
    return 0;
}
