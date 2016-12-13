#include <stdio.h>
#include <math.h> 
int main()
{
	int total = 1;
	scanf("%d", &total);
	
	for (int i=0; i<total; i++) {
		int number = 1;
		scanf("%d", &number);
		double digit = 1.0;
		for (double j=2; j<=number; j=j+1) {
			digit += log10(j);
		}
		printf("%d\n", (int)digit);
	}
	
	return 0;
} 

 
 
/*	NYOJ69 阶乘数位长度 
 *	方法一:
 *	可设想n!的结果是不大于10的M次幂的数,即n!<=10^M(10的M次方),则不小于M的最小整数就是 n!的位数，对
 *	该式两边取对数，有 M =log10^n! 即：M = log10^1+log10^2+log10^3...+log10^n 循环求和,就能算得M值，
 *	该M是n!的精确位数。当n比较大的时候，这种方法方法需要花费很多的时间。
 *	
 *	方法二:
 *	利用斯特林（Stirling）公式的进行求解。下面是推导得到的公式：
 *	res=(long)( (log10(sqrt(4.0*acos(0.0)*n)) + n*(log10(n)-log10(exp(1.0)))) + 1 );
 *	当n=1的时候，上面的公式不适用，所以要单独处理n=1的情况！
 *	有关斯特林（Stirling）公式及其相关推导，这里就不进行详细描述，有兴趣的话可看这里。
 *	这种方法速度很快就可以得到结果。详细证明如下：
 *	http://episte.math.ntu.edu.tw/articles/mm/mm_17_2_05/index.html
*/
//#include<iostream>
//#include <cmath>
//using namespace std;
//int normal(double n)
//{
//	double x=0;
//	while(n)
//	{
//		x +=log10(n);
//		n--;
//	}
//	return (int)x+1;
//}
//long stirling(double n)
//{
//	long x=0;
//	if( n ==1 )
//		x = 1;
//	else
//	{
//		x = (long)( (log10(sqrt(4.0*acos(0.0)*n)) + n*(log10(n)-log10(exp(1.0)))) + 1 );
//	} 
//	return x;
//}
//int main()
//{
//	int n;
//	cin>>n;
//	while(n--)
//	{
//		int x;
//		cin>>x;
//		cout<<stirling(x)<<endl;
//	}
//	return 0;
//}                

