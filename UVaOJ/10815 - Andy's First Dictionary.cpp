#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

int main()
{
    freopen("INPUT.txt", "r", stdin);
    freopen("OUTPUT.txt", "w", stdout);

    string words, buffer;
    set<string> dictionary;
    while (cin >> words) {
        for (int i = 0; i < words.length(); i++)
            if (isalpha(words[i]))
                words[i] = tolower(words[i]);
            else
                words[i] = ' ';

        stringstream ss(words);
        //把words变成了输入流ss，从ss中读string到buffer
        while (ss >> buffer)
            dictionary.insert(buffer);
    }

    for (set<string>::iterator it = dictionary.begin(); it != dictionary.end(); it++)
        //iterator类似于指针
        cout << *it << endl;

    return 0;
}
