#include <stdio.h>
#include <string.h>

int main()
{
	int n = 0;
	scanf("%d", &n);
	while (n--) {
		char s[100];
		scanf("%s", s);
		
		int len = strlen(s);
		for (int i = 1; i < len; i++) {			
			if (len % i == 0) {		//周期是长度的因子 
				for (int j = i; j < len; j = j + i)	//周期为i 
					for (int k = 0; k < i; k++)		//第一个周期 
						if (s[k] != s[j + k])	//其余周期的与第一个周期的逐个比较 
							goto next;
				
				printf("%d", i);
				break;
			}
			
			next:
				
			if (i == (len - 1))
				printf("%d", len);
		}
				
		if (len == 1)	//特殊情况 
			printf("1");			
		if (n >= 1)
			printf("\n");	
	}
    	
    return 0;
}
