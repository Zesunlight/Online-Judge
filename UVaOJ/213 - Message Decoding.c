#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int header[8][256]; //设大一些
int ch = 0; //全局变量最好少用

int leap()  //跳过空格
{
    int ch = getchar();
    while (ch == '\n' || ch == '\r' || ch == '\t')
        ch = getchar();
    return ch;
}

int read_header()   //按长度存起来
{
    memset(header, 0, sizeof(header));

    ch = leap();
    if (ch == EOF)
        return 0;
    header[1][0] = ch;

    for (int i = 2; i <= 7; i++) {
        for (int j = 0; j < (1 << i) - 1; j++) {
            ch = getchar();
            if (ch == '\n' || ch == '\r' || ch == '\t')
                return 1;
            header[i][j] = ch;
        }
    }

    return 1;
}

int read_key(int digit) //二进制转十进制
{
    int number = 0;
    while (digit--)
        number = (number << 1) + leap() - '0';
    return number;
}

int main()
{
//   freopen("INPUT.txt", "r", stdin);

    while (read_header()) {
//    for (int i = 1; i <= 7; i++) {
//        for (int j = 0; j < (2 << i) - 1; j++) {
//            if (header[i][j] != 0)
//                printf("%c", header[i][j]);
//        }
//    }
        while (1) {
            int len = read_key(3);
            if (len == 0)
                break;

            int decode = read_key(len);
            while (decode != ((1 << len) - 1)) {
                printf("%c", header[len][decode]);
                decode = read_key(len);
            }
        }
        printf("\n");
    }

	return 0;
}
