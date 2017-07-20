#include <stdio.h>

int sum(int n)
{
	int t = n, result = 0;;
	for (int i = 2; t < 1000; i++) {
		result += t;
		t = n * i;
	}
	return result;
}
int main()
{

	printf("%d\n", sum(3) + sum(5) - sum(15));
	return 0;
}
