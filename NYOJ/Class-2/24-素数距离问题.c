#include <stdio.h>
#include <math.h>
int isPrime(long int n);
int main()
{
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		long int n = 0;
		scanf("%ld", &n);
		if (n == 1) {
			printf("2 1\n");
			continue;
		}
		if (isPrime(n)) {
			printf("%ld 0\n", n);
		} else {
			for (int i = 1; i <= n - 3; i++) {
				if (isPrime(n - i)) {
					printf("%ld %d\n", n - i, i);
					break;
				}
				if (isPrime(n + i)) {
					printf("%ld %d\n", n + i, i);
					break;
				}
			}
		}		
	}
	return 0;
} 
int isPrime(long int n)
{
	if (n == 1)
		return 0;
	for (int i = 2; i <= (long int)sqrt(n); i++) {
		if (n % i == 0)
			return 0;
	}
	return 1;
}

---------------------------------------------------

#include<iostream>
#include<cmath>
using namespace std;

bool isprime(int n)
{
	for(int k=2;k<=sqrt((double)n);k++)
		if((n%k)==0)
			return false;
	return true;
}
int main()
{
	int n;
	cin>>n;
	while(n--)
	{
		int num,i,j;		
		cin>>num;
		if(num==1)
		{
			cout<<"2 1"<<endl;
			continue;
		}
		for(i=num;!isprime(i);i--);	
		for(j=num;!isprime(j);j++);	
		
		if((num-i)<(j-num))
			cout<<i<<' '<<(num-i)<<endl;
		else if((num-i)>(j-num))
			cout<<j<<' '<<(j-num)<<endl;
		else if((num-i)==(j-num))
			cout<<i<<' '<<(num-i)<<endl;
	}
}        
