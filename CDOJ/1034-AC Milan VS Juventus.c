#include <stdio.h>
#include <math.h>
int main ()  								
{	
	int a, b;
	scanf("%d%d", &a, &b);

	if (a == b)
		printf("No");
	else {
		if (a > 5 || b > 5) {
			if (abs(a - b) >= 2)
				printf("No");
			else
				printf("Yes");
		} else {
			if (abs(a - b) >= 3) {
				if ((a == 0 && b == 3) || (a == 3 && b == 0) || (a == 1 && b == 4) || (a == 4 && b == 1))
					printf("Yes");
				else
					printf("No");
			} else
				printf("Yes");
		}
	}
	
//	printf("%d", n);		
	return 0;
}

