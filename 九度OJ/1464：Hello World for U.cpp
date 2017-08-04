#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{

	string s("abc");
	while (cin >> s) {
		int len = s.length();
		int n1 = (len + 2) / 3 - 1;
		int n2 = len - 2 * n1;
		for (int i = 0; i < n1; i++) {
			cout << s[i];
			for (int j = 0; j < n2 - 2; j++)
				cout << ' ';
			cout << s[len - i - 1] << endl;
		}
		cout << s.substr(n1, n2) << endl;
	}

    return 0;
}

/****************************************************
    Problem: 1464
    Website: http://ac.jobdu.com/problem.php?pid=1464
    User: ZYZ
    Language: C++
    Result: Accepted
    Time: 10 ms
    Memory: 1520 kb
*****************************************************/
