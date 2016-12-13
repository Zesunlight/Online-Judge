#include <stdio.h>
int main()
{
	int a,b,c;
	scanf("%d %d %d", &a, &b, &c);
	
	int amount=10;
	while( amount<=100 ){
		if(!(((amount-a)%3)||((amount-b)%5)||((amount-c)%7))){
			printf("%d", amount);
			break;
		}
		amount++;
	}
	
	if(amount>100){
		printf("No answer");
	} 
	return 0;
 } 
 
//#include<iostream>
//using namespace std;
//int main()
//{
//	int a,b,c;
//	cin>>a>>b>>c;
//	int n=(a*70+b*21+c*15)%105;
//	if(n>100||n<10) cout<<"No answer"<<endl;
//	else cout<<n<<endl;
//}         
