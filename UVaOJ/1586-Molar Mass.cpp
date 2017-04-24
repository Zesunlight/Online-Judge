#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main()
{
	int n = 1;
	scanf("%d", &n);
	
	char s[90] = {"\0"};
	while (n--) {
		scanf("%s", s);
		double weight = 0.0;
		int len = strlen(s);
		for (int i = 0; i < len; i++) {
			int num = 1;
			if (s[i] == 'C') {
				if (isdigit(s[i+1])) {
					if (isdigit(s[i+2])) {
						num = (s[i+1] - '0') * 10 + (s[i+2] - '0');
						i += 2;
					} else {
						num = s[i+1] - '0';
						i++;
					}						
				}
				weight += num * 12.01;
			} else if (s[i] == 'H') {
				if (isdigit(s[i+1])) {
					if (isdigit(s[i+2])) {
						num = (s[i+1] - '0') * 10 + (s[i+2] - '0');
						i += 2;
					} else {
						num = s[i+1] - '0';
						i++;
					}						
				}
				weight += num * 1.008;
			} else if (s[i] == 'O') {
				if (isdigit(s[i+1])) {
					if (isdigit(s[i+2])) {
						num = (s[i+1] - '0') * 10 + (s[i+2] - '0');
						i += 2;
					} else {
						num = s[i+1] - '0';
						i++;
					}						
				}
				weight += num * 16.00;
			} else if (s[i] == 'N') {
				if (isdigit(s[i+1])) {
					if (isdigit(s[i+2])) {
						num = (s[i+1] - '0') * 10 + (s[i+2] - '0');
						i += 2;
					} else {
						num = s[i+1] - '0';
						i++;
					}						
				}
				weight += num * 14.01;
			}
		}
		printf("%.3lf\n", weight);
	}
	
	
	return 0;
}
