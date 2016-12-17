#include <stdio.h>

int main()
{
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		int budget = 0;
		int all_save = 0;
		int remain = 0;//last month's money that hasn't used
		int judge = 1;
		int accident = 0;
		for (int i = 0; i < 12; i++) {
			scanf("%d", &budget);
			int rest = 300 + remain - budget;//the money that I don't need
			if (rest < 0) {
				accident = i + 1;
				judge = 0;
			}
			int save = (rest / 100) * 100;
			all_save += save;
			remain = rest - save;
		}
		if (judge)
			printf("%d\n", remain + (int)(all_save * 1.2 * 2 + 1) / 2);
		else 
			printf("-%d\n", accident);			
	}
	
	return 0;
}

-----------------------------------------------------
 
#include <stdio.h>
int main()
{ 
	//freopen("1.txt","r",stdin);
	int n,m[20],i,t,s;
	int sum;
	scanf("%d",&n);
	while(n--)
	{
		for(i=0;i<12;i++)
		{
			scanf("%d",&m[i]);
		}
		s=0;
		t=0;
		for(i=0;i<12;i++)
		{
			s+=(t+300-m[i])/100;
			t=(t+300-m[i])%100;
			if(t<0)
			{printf("%d\n",-(i+1));break;}
			
			if(i==11)
		{
				sum=s*100*1.2+t+0.5;
				printf("%d\n",sum);
			}
		}
	}return 0;
}
