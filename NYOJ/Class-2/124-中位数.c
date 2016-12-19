#include <stdio.h>

int main()
{
	int total = 0;
	scanf("%d", &total);
	int x = 0, n = 0;
	while (total--) {
		int n = 0;
		scanf("%d", &n);
		int sort[n];
		for (int i = 0; i < n; i++)
			scanf("%d", &sort[i]);
		
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < n - i; j++) {
				if (sort[j] > sort[j+1]) {
					int temp = sort[j+1];
					sort[j+1] = sort[j];
					sort[j] = temp;
				}
			}
		}
		printf("%d\n", sort[n / 2]);
	}
	
	return 0;
}

-----------------------------------------------
 
#include<iostream>
#include<algorithm>
using namespace std;
int a[1003];
int main()
{	
	int n,x;
	cin>>n;
	while(n--)
	{
		cin>>x;
		for(int i=0;i<x;i++)
			cin>>a[i];
		nth_element(a,a+x/2,a+x);
		cout<<a[x/2]<<endl;
	}
}        
