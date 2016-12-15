#include <stdio.h>

int main()
{
	int n = 0, m = 0;
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		scanf("%d%d", &n, &m);
		//m is a prime
		int sum = 0;
		while (n >= m) {
			n /= m;
			sum += n;
		}
		printf("%d\n", sum);
	}
	
	return 0;
} 
