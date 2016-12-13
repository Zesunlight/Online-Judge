#include <stdio.h>
#include <math.h>
#define bool int
#define false 0
#define true 1
bool isPrime(int n);

int main()
{
	int n = 0;
	int total = 0;
	scanf("%d", &total);
	
	while (total--) {
		scanf("%d", &n);
		int sum = 0;
		
		for (int i = 0; i < n; i++) {
			int math = 0;
			scanf("%d", &math);
			if (math >= 2 && isPrime(math))
				sum += math;
		}
		
		printf("%d\n", sum);	
	}
	
	return 0;
}

bool isPrime(int n)
{
	for (int i = 2; i <= sqrt(n); i++)
		if ( n % i == 0)
			return false;
	
	return true;
}
