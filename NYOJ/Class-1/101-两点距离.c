#include <stdio.h>
#include <math.h>

int main()
{
	int total = 1;
	scanf("%d", &total);
	
	float x1, y1, x2, y2;
	for (int i=0; i<total; i++) {
		scanf("%f%f%f%f", &x1, &y1, &x2, &y2);
		printf("%.2f\n", sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)));
	}

	return 0;
} 

#include<iostream>
#include<math.h>
#include<iomanip>
using namespace std;
int main()
{
	/*freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);*/

	double x1,x2,y1,y2,m;
	double a;
	cin>>m;
	while(m--)
	{
		cin>>x1>>y1>>x2>>y2;
    	a=sqrt((double)((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)));
		cout.setf(ios::fixed); 
    	cout<<setprecision(2)<<a<<endl;
	}
	return 0;
}
