#include <stdio.h>
int main()
{
    int total = 0;
    scanf("%d", &total);
    while (total--) {
        int m = 0;
        unsigned long int n = 0;
        scanf("%lu%d", &n, &m);
        int sum = 0;
        for ( ; n >= m; n /= m)
            sum += n / m;
        printf("%d\n", sum);
    }
    return 0;
}
