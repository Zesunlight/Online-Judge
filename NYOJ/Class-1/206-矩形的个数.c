#include <stdio.h>

int main()
{
//	int total = 0;
//	scanf("%d", &total);
//	while (total--) {
//		
//		printf("%d\n", result);
//	}

	long long int A = 0, B = 0;
	while (scanf("%lld%lld", &A, &B) != EOF) {
		printf("%lld\n", A * (A+1) * B * (B+1) / 4);
	}
	
	return 0;
}
