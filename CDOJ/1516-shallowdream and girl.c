#include <stdio.h>

int sum(int a1, int a2, int a3);
int main()
{
	int a1 = 0, a2 = 0, a3 = 0;
	scanf("%d %d %d", &a1, &a2, &a3);
	
	int total = 0;
	total = sum(a1, a2, a3);
	
	printf("%d", total);
	return 0;
}

int sum(int a1, int a2, int a3)
{
	int sum = 0;
	if (a1 == 0 || a2 == 0 || a3 == 0) {
		if (a1 == 0 && a2 == 0 && a3 == 0)
			sum = 0;
		if (a1 != 0 && a3 == 0)
			sum = a1 + 2*a2;
		if (a1 == 0 && (a2 == 0 || a3 ==0))
			sum = a2 + a3;
		if (a2 == 0) {
			if (a1 >= 2)
				sum = a1 + 3*a3;
			else
				sum = 2*a3 + 1;
		}
		if (a1 == 0) {
			if (a3 == 1)
				sum = 2*a2 + 1;
			else if (a2 <= 2)
				sum = (a2 + 1) * a3 + a2;
			else
				sum = 2*a2 + 3*a3 -2;
			/* 3,6,9,12,15 ...	--->3*a3
			   2,5,8,11,14 ...	--->3*a3-1
			   4,7,10,13,16 ...	--->3*a3+1    一共3*a3种			
   			全部的3都用上，再一个一个加2
			3*a3+2, 3*a3+4, 3*a3+6 ...
			少用一个3，再一个个加2
			3*a3-3+2, 3*a3+1, 3*a3+3 ...	一共2*a2种
			与前面重复两个，减去2			*/	
		}	
	} else
		sum =  a1 + 2*a2 + 3*a3;
	return sum;
}


//BNUOJ 52297
