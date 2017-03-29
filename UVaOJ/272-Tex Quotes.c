#include <stdio.h>

int main()
{
	int t = 1;
	char c = '\0';
	while ((c = getchar()) != EOF) {
		if (c == '"') {
			printf("%s", t ? "``" : "''");
			t = !t;
		} else 
			printf("%c", c);
		
	}
	return 0;
}

