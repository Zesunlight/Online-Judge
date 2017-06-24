#include <stdio.h>
#include <string.h>
#include <ctype.h>
void judge(char *s, char *t);
char s[1000000] = "\0", t[1000000] = "\0";
int main()
{			
	while ((scanf("%s%s", s, t)) != EOF) {
		if (strlen(s) > strlen(t))
			printf("No\n");
		else if (strlen(s) < strlen(t))
			judge(s, t);
		else
			printf("%s\n", strcmp(s, t) ? "No" : "Yes");		
	}
		
	return 0;
}

void judge(char *s, char *t)
{
	int len_s = strlen(s);
	int len_t = strlen(t);
	int j = 0;
	for (int i = 0; i < len_t; i++)
		if (s[j] == t[i])
			j++;
	if (j < len_s)
		printf("No\n");
	else
		printf("Yes\n");
}
