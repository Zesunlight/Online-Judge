#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
void mergeSort(int start, int end);

vector<long long int, allocator<long long int>> number, temp;
long long int time = 0;
int main()
{
	int n = 0;
	scanf("%d", &n);
	long long int m = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%lld", &m);
		number.push_back(m);
	}

	mergeSort(0, n);

    printf("%lld", time);

	return 0;
}

void mergeSort(int start, int end)
{
	if (end - start <= 1)
		return;

	int mid = (start + end) / 2;
	mergeSort(start, mid);
	mergeSort(mid, end);

	int former = start, latter = mid;
	while (former < mid && latter < end) {
		if (number[former] < number[latter]) {
			temp.push_back(number[former++]);
		} else {
            temp.push_back(number[latter++]);
            time += mid - former;
		}
	}
	while (former < mid) {
        temp.push_back(number[former++]);
	}

	while (latter < end)
		temp.push_back(number[latter++]);

	for (int i = start; i < end; i++) {
		number.at(i) = temp.at(i - start);
	}
	temp.clear();
}
