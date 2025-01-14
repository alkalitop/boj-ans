#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int a = 0, b = 1, t;
    for (int i = 0; i < n; i++) {
        t = b;
        b += a;
        a = t;
    }
    cout << a;
    return 0;
}
