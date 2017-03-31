#include <stdio.h>

int main()
{
    int x = 1, y = 1, n = 1;
    scanf("%d%d%d", &x, &y, &n);
    int able = 0;
    if ((x+y) % (2*n+1) == 0) {
    	int temp = (x+y) / (2*n+1);
    	if ((temp + y - x) % 2 == 0) {
    		int k = (temp + y - x) / 2;
    		int l = (temp - y + x) / 2;
    		if ((k >= 0) && (l >= 0))
    			able = 1;
		}
	}
	
	if (able)
		printf("Yes");
	else
		printf("No");
    	
    return 0;
}
