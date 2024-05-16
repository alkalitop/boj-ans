#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int m = 0, n;
    float t = 0;
    scanf("%d\n", &n);
    
    int *s = malloc(sizeof(float) * n);
    
    for (int i = 0; i < n; i++) {
        scanf("%d ", &s[i]);
        if (m < s[i]) m = s[i];
    }
    
    for (int i = 0; i < n; i++) {
        t += ((float)s[i])/((float)m)*100.0f;
    }
    
    t /= n;
    printf("%f ", t);
    
    return 0;
}
