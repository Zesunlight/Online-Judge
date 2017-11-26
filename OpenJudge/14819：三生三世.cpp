#include <iostream>
#include <algorithm>
#include <list>
#include <cstring>
#include <fstream>
using namespace std;

class TV_Drama{
	public:
	char name[100];
	int actor;
	int story;
	int acting_skill;
// 在此处补充你的代码
    TV_Drama(const char a[], int b, int c, int d):actor(b), story(c), acting_skill(d) {
        strcpy(name, a);
    }
    bool operator < (TV_Drama& that) {
        return actor > that.actor;
    }
};

void Printer(TV_Drama& it) {
    cout << it.name << ';';
}

bool comparator_1(TV_Drama& that_, TV_Drama& that) {
    return that_.story > that.story;
}

class comparator_2 {
public:
    bool operator () (TV_Drama& that_, TV_Drama& that) {
        return that_.acting_skill > that.acting_skill;
    }
};

int main() {

    list<TV_Drama> lst;
	int n;

	cin>>n;
	char  _name[100];
	int _actor, _story, _acting_skill;
	for (int i=0; i<n; i++){
        cin.ignore();
        cin.getline(_name,100);
        cin>>_actor>>_story>>_acting_skill;
		lst.push_back(TV_Drama(_name, _actor, _story, _acting_skill));
	}

	lst.sort();
	for_each(lst.begin(), lst.end(), Printer);
	cout<<endl;

	lst.sort(comparator_1);
	for_each(lst.begin(), lst.end(), Printer);
	cout<<endl;

	lst.sort(comparator_2());
	for_each(lst.begin(), lst.end(), Printer);
	cout<<endl;

	return 0;
}

/****************************************************
    Problem: 013:编程填空：三生三世
    Website: http://cxsjsxmooc.openjudge.cn/2017t3fallfinal/013/
    User: ZhaoYongze
    Language: C++
    Result: Accepted
    Time: 1 ms
    Memory: 128 kB
    Date: 2017.11.26
*****************************************************/
