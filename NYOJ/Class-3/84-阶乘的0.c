#include <stdio.h>

int main()
{
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		long long int num = 0; 
		scanf("%lld", &num);
		int zero = 0;
		for ( ; num >= 5; num /= 5)
			zero += num / 5;
		printf("%d\n", zero);
	}
	
	return 0;
}

