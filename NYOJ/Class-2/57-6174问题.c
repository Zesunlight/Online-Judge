#include <stdio.h>
int sort(int n);

int main()
{
	int n = 0;
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		scanf("%d", &n);
		int count = 0;
		for ( ; ; ) {
			count++;
			if ( sort(n) == n) {
				printf("%d\n", count);
				break;
			} else
				n = sort(n);		
		}	
	}
	
	return 0;
}

int sort(int n)
{
	int digit[3] = {0};
	digit[0] = n / 1000;
	digit[1] = n / 100 - digit[0] * 10;
	digit[2] = n / 10 - digit[0] * 100 - digit[1] * 10;
	digit[3] = n % 10;
	
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3 - i; j++) {
			if (digit[j] > digit[j+1]) {
				int temp = digit[j];
				digit[j] = digit[j+1];
				digit[j+1] = temp;	
			}
		}
	}
	int max = 1000*digit[3] + 100*digit[2] + 10*digit[1] + digit[0];
	int min = 1000*digit[0] + 100*digit[1] + 10*digit[2] + digit[3];
	return max - min;
}
