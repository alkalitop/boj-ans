#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d ", &n);

    if (n == 1) return 0;

    int d = 2;
    while (n > 1) {
        if (n % d == 0) {
            printf("%d\n", d);
            n /= d;
        }
        else d++;
    }

    return 0;
}
