#include <stdio.h>
#include <math.h>
int main()
{
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		int x = 0;
		scanf("%d", &x);
		int i = (int)(sqrt(2 * x + 0.25) + 0.5);
		
		if (x == i * (i - 1) / 2)
			i = i - 1;
		int rest = x - i * (i - 1) / 2;
		
		if (i % 2 == 0)
			printf("%d/%d\n", rest, i - rest + 1);
		else
			printf("%d/%d\n", i - rest + 1, rest);
			
	}
	
	return 0;
}

-------------------------------------------
 
#include <stdio.h>
#include <math.h>
main()
{
	int n,m,x,y;
	scanf("%d\n",&m);
	while(m--)
	{
		scanf("%d",&n);
		x=(int)(sqrt(2*n)-0.5);
		y=n-x*(x+1)/2;
		if(x%2==0)
			printf("%d/%d\n",x+2-y,y);

		else
			printf("%d/%d\n",y,x+2-y);
	}
}
