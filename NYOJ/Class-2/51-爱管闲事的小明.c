#include <stdio.h>

int main()
{
	int total = 0;
	scanf("%d", &total);
	while (total--) {
		int tree[10001] = {0};
		int length = 0;
		scanf("%d", &length);
		int area = 0;
		scanf("%d", &area);
		while (area--) {
			int begin = 0, end = 0;
			scanf("%d%d", &begin, &end);
			for (int i = begin; i <= end; i++)
				tree[i] = 1;
		}
		int sum = 0;
		for (int i = 0; i <= length; i++)	
			if (tree[i] == 0)
				sum++;
		printf("%d\n", sum);
	}
	
	return 0;
} 

----------------------------------------------
 
#include<iostream>
#include<numeric>
#include<vector>
using namespace std;
int main()
{
	int n,beg,end,L,M;
	cin>>n;
	
	while(n--)
	{
		cin>>L>>M;
		vector<bool> have(L+1,true);
		while(M--)
		{
			cin>>beg>>end;
			for(int i=beg;i<=end;i++)
				have[i]=false;
		}
	//	cerr<<100-n<<endl;
		cout<<accumulate(have.begin(),have.end(),0)<<endl;
	}
	
}

-----------------------------------------------------

#include<iostream>
using namespace std;
const int maxn=10005;
int num[maxn];
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        int L,M;
        scanf("%d%d",&L,&M);
        for(int i=0; i<=L; i++)
            num[i]=0;
        int left,right;
        while(M--)
        {
            scanf("%d%d",&left,&right);
            num[left]--;
            num[right]++;
            //表示那一段路 
        }
        int sum=0;//总数
        int flag=0;//标记变量
        for(int i=0; i<=L; i++)
        {
            flag+=num[i];
            if(flag==0) {
                sum++;
            	if(num[i]>0)	//端点的问题 
                	sum--;
			}          
        }
        printf("%d\n",sum);
    }
    return 0;
}

