#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char answer[50] = "\0";
    char guess[30] = "\0";
    int round = 0;
 //   freopen("INPUT.txt", "r", stdin);
    while (scanf("%d%s%s", &round, answer, guess) != EOF && round != -1) {
        int len_a = strlen(answer);
        int times = 7;
        int remain = len_a;
        int len_g = strlen(guess);
        printf("Round %d\n", round);
        for (int i = 0; i < len_g; i++) {
            int get = 0;
            for (int j = 0; j < len_a; j++) {
                if (guess[i] == answer[j]) {
                    answer[j] = ' ';
                    remain--;
                    get = 1;
                }
            }
            if (get == 0)
                times--;

            if (remain == 0) {
                printf("You win.\n");
                break;
            }
            if (times == 0) {
                printf("You lose.\n");
                break;
            }
        }

        if (times > 0 && remain > 0)
            printf("You chickened out.\n");
    }

	return 0;
}
