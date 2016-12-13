#include <stdio.h>

int main()
{
	int total = 0;				//输入total组数据 
	scanf("%d", &total);
	int group[7] = {0};	//每组有14个数 
	
	for (int i = 0; i < total; i++) {
		for (int j=0; j<7; j++) {
			int a = 0, b = 0;
			scanf("%d %d", &a, &b);	//存储输入的一组数据 
			group[j] = a + b;
		}
		
		int max = 0;
		int save = 0;
		for (int k = 0; k < 7; k++) 
			if (group[k] > max) {
				max = group[k];
				save = k;
			}				
		
		if (max <= 8)
			printf("0\n");		//输出结果 
		else
			printf("%d\n", save + 1);
	}
	
	return 0;
} 


 
//#include <iostream>
//using namespace  std;
//int main()
//{
//	int n;
//	cin>>n;
//	while(n--)
//	{
//		int a,b,max=8,d=0;
//		for (int i=0;i<7;i++)
//		{
//			cin>>a>>b;
//			if(a+b>max)
//			{
//				d=i;
//				max=a+b;
//			}
//		}
//	if(max>8) cout<<d+1<<endl;
//	else cout<<"0"<<endl;
//	}
//	return 0;
//}    
