#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
	char s[5][6];
	int empty_x = 0, empty_y = 0;
	char action;
	int count = 0;
	for (int i = 0; i < 5; i++) {
		gets(s[i]);
		if (s[0][0] == 'Z')
			break;
	}
		
	while (s[0][0] != 'Z') {
		//find the empty position
		for (int i = 0; i < 5; i++) 
			for (int j = 0; j < 5; j++)
				if (s[i][j] == ' ') {
					empty_x = i;
					empty_y = j;
				}
				
		//moving
		int flag = 1;
		scanf("%c", &action);
		while (action != '0') {
			if (flag)
				switch(action) {
					case 'A':
						if (empty_x - 1 >= 0) {
							s[empty_x][empty_y] = s[empty_x - 1][empty_y];
							empty_x--;
						} else
							flag = 0;
						break;
					case 'B':
						if (empty_x + 1 <= 4) {
							s[empty_x][empty_y] = s[empty_x + 1][empty_y];
							empty_x++;
						} else
							flag = 0;
						break;
					case 'L':
						if (empty_y - 1 >= 0) {
							s[empty_x][empty_y] = s[empty_x][empty_y - 1];
							empty_y--;
						} else
							flag = 0;
						break;
					case 'R':
						if (empty_y + 1 <= 4) {
							s[empty_x][empty_y] = s[empty_x][empty_y + 1];
							empty_y++;
						} else
							flag = 0;
						break;
				}
			scanf("%c", &action);			
		}
		
		//out put result
		s[empty_x][empty_y] = ' ';
		count++;
		if (flag == 0)
			printf("Puzzle #%d:\nThis puzzle has no final configuration.\n", count);
		else {
			printf("Puzzle #%d:\n", count);
			for (int i = 0; i < 5; i++) {
				for (int j = 0; j < 5; j++)
					printf("%c ", s[i][j]);
				printf("\n");
			}
		}
		
		//scanf the next puzzle
//		memset(s, '\0', sizeof(s));
		for (int i = 0; i < 5; i++) {
			gets(s[i]);
			if (!isalpha(s[0][0]))
				i--;
			else if(s[0][0] == 'Z')	
				break;
		}			
	}
	
	return 0;
}
