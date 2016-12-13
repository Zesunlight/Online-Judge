#include <stdio.h>
int main()
{
	int number[5] = {0};
	int i = 0;

	for ( i=0; i<5; i++){
		scanf("%d", &number[i]);
	}
	int min=number[0];
	int max=number[0];
	
	for ( i=1; i<5; i++){
		if( min>number[i]){
			min = number[i];
		}
		if( max<number[i]){
			max = number[i];
		}
	}
	
	printf("%d %d", min, max);
	
	return 0;
}
 
//#include<iostream>
//#include<iterator>
//#include<algorithm>
//using namespace std;
//int main()
//{
//	int a[5];
//	copy(istream_iterator<int>(cin),istream_iterator<int>(),a);
//	cout<<*min_element(a,a+5)<<" "<<*max_element(a,a+5)<<endl;
//}        
