#include <stdio.h>

int main()
{
	long long term[3] = {1, 2, 3};
	long long result = 2;
	for (int i = 3; ; i++) {
		term[i % 3] = term[(i-1) % 3] + term[(i-2) % 3];
		if (term[i % 3] > 4000000)
			break;
		if ((i-1) % 3 == 0)
			result += term[i % 3];
	}
	printf("%lld\n", result);
	return 0;
}
