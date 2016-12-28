#include <stdio.h>

int main()
{
	int total = 0;
	scanf("%d", &total);
	unsigned long int haha[40] = {0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 
		610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 
		196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 
		14930352, 24157817, 39088169, 63245986, 102334155};
	//先用递归得到前四十项 
	while (total--) {
		int m = 0;
		scanf("%d", &m);
		printf("%lu\n", haha[m - 1]);
	}

//	while (scanf("%d%d", &x, &n) != EOF) {
//		
//		printf("%lld\n", result);
//	}
	
	return 0;
}

------------------------------------------

#include<iostream>
using namespace std;
int main()
{
	int f[41]={0,0,1,2};
	for(int i=4;i<=40;i++)
	{
	   f[i]=f[i-1]+f[i-2];
	}
	int k;
	cin>>k;
	for(int i=0;i<k;i++)
	{
	   int j;
	   cin>>j;
	   cout<<f[j]<<endl;
	}
}

