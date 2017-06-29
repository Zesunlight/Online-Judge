#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
 //   freopen("INPUT.txt", "r", stdin);
    int N, k, m;
    int applicant[25] = {0};
    while (scanf("%d%d%d", &N, &k, &m) != EOF) {
        if (N == 0 && k == 0 && m == 0)
            break;
        int clock = N - 1, c_clock = 0;
        for (int i = 0; i < N; i++)
            applicant[i] = 1;
        int remain = N;
        while (remain > 0) {
            for (int i = 0; i < k - 1; i++) {
                while (applicant[c_clock] == 0)
                    c_clock = (c_clock + 1) % N;
                c_clock = (c_clock + 1) % N;
            }
            while (applicant[c_clock] == 0)
                c_clock = (c_clock + 1) % N;

            for (int i = 0; i < m - 1; i++) {
                while (applicant[clock] == 0)
                    clock = (clock - 1 + N) % N;
                clock = (clock - 1 + N) % N;
            }
            while (applicant[clock] == 0)
                clock = (clock - 1 + N) % N;
            if (c_clock != clock) {
                applicant[clock] = 0;
                remain--;
            }

            applicant[c_clock] = 0;
            remain--;

            if (c_clock == clock)
                printf("%3d", (c_clock + 1));
            else
                printf("%3d%3d", (c_clock + 1), (clock + 1));

            if (remain > 0)
                printf(",");
            else
                printf("\n");
        }
    }

	return 0;
}
