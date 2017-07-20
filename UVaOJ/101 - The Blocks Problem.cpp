#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

vector<int> block[30];  //vector<int> 类型的数组，30个
int number = 0;

void find_block(int name, int& position, int& height)
{
    for (position = 0; position < number; position++)
        for (height = 0; height < block[position].size(); height++)
            if (block[position][height] == name)
                return;
}

//returning any blocks that are stacked on top of blocks height to their initial positions.
//在position中高度为height上的block回到初始位置
void returning(int position, int height)
{
    for (int i = height + 1; i < block[position].size(); i++) {
        int n = block[position][i]; //第n块
        block[n].push_back(n);  //归位
    }
    block[position].resize(height + 1); //改变大小，height上面的都移走了
}

//pile here over there
void pile_over(int here, int height, int there)
{
    for (int i = height; i < block[here].size(); i++)
        block[there].push_back(block[here][i]); //移到there尾部
    for (int i = block[here].size(); i > height; i--)
        block[here].pop_back(); //删除here尾部的
}

int main()
{
//    freopen("INPUT.txt", "r", stdin);
//    freopen("OUTPUT.txt", "w", stdout);

    scanf("%d", &number);
    for (int i = 0; i < number; i++)
        block[i].push_back(i);  //向block[i]尾部添加元素i

    int from = 0, to = 0;
    string s1, s2;
    while (cin >> s1 >> from >> s2 >> to) {
        int from_position = 0, from_height = 0;
        int to_position = 0, to_height = 0;
        find_block(from, from_position, from_height);
        find_block(to, to_position, to_height);

        if (from_position == to_position)
            continue;
        if (s1 == "quit")
            break;

        //清理上面的块
        if (s1 == "move")
            returning(from_position, from_height);
        if (s2 == "onto")
            returning(to_position, to_height);

        //包括height的块都移到to上
        pile_over(from_position, from_height, to_position);


    }

    for (int i = 0; i < number; i++) {
        printf("%d:", i);
        for (int j = 0; j < block[i].size(); j++)
            printf(" %d", block[i][j]);
        printf("\n");
    }

    return 0;
}
