#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <cstdio>
#include <cstdlib>
using namespace std;

map<string, string> dictionary;
int main()
{
//    ifstream cin("INPUT.txt");
//    if (cin.fail()) {
//        cout << "open file failed!";
//        return 0;
//    }
//    ofstream cout("OUTPUT.txt");
    char word[15], english[15];
    string s1, s2;
    while (cin.peek() != '\n') {
        scanf("%s %s", english, word);
        s1 = english;
        s2 = word;
        cin.get();
        dictionary.insert(make_pair(s2, s1));
        //dictionary[word] = english;
        //dictionary.insert(map<char*, char*>::value_type(word, english));
    }
    map<string, string>::iterator it;
//    for (it = dictionary.begin(); it != dictionary.end(); it++)
//        printf("%s\t%s\n", it->first.c_str(), it->second.c_str());
    while (scanf("%s", word) != -1) {
            s1 = word;
        it = dictionary.find(s1);
        if (it != dictionary.end())
            printf("%s\n", it->second.c_str());
        else
            printf("eh\n");
    }

//    cout.close();
//    cin.close();
    return 0;
}
