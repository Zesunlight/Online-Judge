#include <iostream>
#include <set>
#include <functional>   
#include <iterator>
#include <cstdio>
using namespace std;

multiset<long long int, greater<long long int>> number;

int main()
{
	int n = 0, k = 0;
	long long int m = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%lld", &m);
		number.insert(m);
	}
	scanf("%d", &k);
	multiset<long long int, greater<long long int>>::iterator it = number.begin();
	for (; k > 0; k--) {
		cout << *it << endl;	
		it++;
	}

	return 0;
}
