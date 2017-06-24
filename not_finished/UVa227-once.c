#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main()
{		
	char s[7][7];	
	int ascii[128];
	memset(ascii, 0, sizeof(ascii));
	ascii['A'] = ascii['L'] = -1;
	ascii['B'] = ascii['R'] = 1;
	int count = 1;
	char n = '\0';
	scanf("%c", &n);
	while (n != 'Z') {
		memset(s, '\0', sizeof(s));
		s[1][1] = n;
		int x = 3, y = 3;	//the empty position
		for (int i = 2; i <= 25; i++) {
			int x_temp = (i + 4) / 5;
			int y_temp = (i % 5 > 0) ? (i % 5): 5;
			scanf("%c", &s[x_temp][y_temp]);
			if (s[x_temp][y_temp] == ' ') {
				x = x_temp;
				y = y_temp;
			}
			if (s[x_temp][y_temp] == '\n')
				i--;
		}
		
		char action = '\n';
		int flag = 1;	//moving is valid
		while (!(isdigit(action) || isalpha(action)))
			scanf("%c", &action);
		while (action != '0') {
			if (flag) {
				if (action == 'A' || action == 'B') {
					if (s[x + ascii[action]][y] != '\0') {
						s[x][y] = s[x + ascii[action]][y];
						s[x + ascii[action]][y] = ' ';
						x += ascii[action];
					} else
						flag = 0;
				} else if (action == 'L' || action == 'R') {
					if (s[x][y + ascii[action]] != '\0') {
						s[x][y] = s[x][y + ascii[action]];
						s[x][y + ascii[action]] = ' ';
						y += ascii[action];
					} else
						flag = 0;
				} else
					flag = 0;								
			}
					
			scanf("%c", &action);
			while (!(isdigit(action) || isalpha(action)))
				scanf("%c", &action);
		}
			
		if (flag == 0) {
			printf("Puzzle #%d:\n", count);
			printf("This puzzle has no final configuration.\n");
		} else {
			printf("Puzzle #%d:\n", count);
			for (int i = 1; i <= 5; i++) {
				for (int j = 1; j <= 5; j++)
					printf("%c ", s[i][j]);
				printf("\n");
			}			
		}

		scanf("%c", &n);
		while (!isalpha(n))
			scanf("%c", &n);
		count++;
	}	
	return 0;
}
