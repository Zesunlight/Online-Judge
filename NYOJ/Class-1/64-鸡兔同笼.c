#include <stdio.h>

int main()
{
	int total = 1;
	scanf("%d", &total);
	
	int number[total][2];
	int i = 0;
	for( i=0; i<total; i++){
		scanf("%d %d", &number[i][0], &number[i][1]);
	}
	
	int hen=0, rabbit=0;
	for( i=0; i<total; i++){
		hen = (4*number[i][0]-number[i][1])/2;
		rabbit = (number[i][1]-2*number[i][0])/2;
		if( number[i][1]%2 || hen<0 || rabbit<0){
			printf("No answer\n");
		}else {		
			printf("%d %d\n", hen, rabbit);
		}	
	}	
	return 0;
} 

//#include<iostream>
//using namespace std;
//int main()
//{
//	int n,a,b,p,q;
//	cin>>n;
//	while(n--)
//	{
//		cin>>a>>b;
//		q=(b-2*a)/2;
//		p=a-q;
//		if(p<0 ||q<0 || b%2) 
//			cout<<"No answer"<<endl;
//		else 
//			cout<<p<<" "<<q<<endl;
//	}
//}
