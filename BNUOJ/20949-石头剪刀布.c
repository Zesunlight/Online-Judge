#include <stdio.h>

int main()
{
    int x = 1, l = 1;
    scanf("%d%d", &x, &l);
    if (x == l)
    	printf("DRAW");
    else if ((l+1) % 3 == x)
    	printf("XX");
    else
    	printf("LZX");
    	
    return 0;
}