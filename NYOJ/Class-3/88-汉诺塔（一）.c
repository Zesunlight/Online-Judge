#include <stdio.h>
long long int power (int n);
int main ()  								
{	
//	int a, b, c;
//	scanf("%d%d%d", &a, &b, &c);
//	printf("%.3f\n", (a + b + c) / 3.0); 
	
	int N = 1;
	scanf("%d", &N);
	int m = 1;
	while (N--) {
		scanf("%d", &m);
		
		printf("%lld\n", power(m) - 1);
	}
	
//	printf("%d", n);		
	return 0;
}

long long int power (int n)
{
	if (n == 1)
		return 2;
	else {
		long long int t = power(n / 2);
		if (n % 2 == 0)
			return ((t % 1000000) * (t % 1000000)) % 1000000;
		else
			return (2 * (t % 1000000) * (t % 1000000)) % 1000000;
	}	
}

