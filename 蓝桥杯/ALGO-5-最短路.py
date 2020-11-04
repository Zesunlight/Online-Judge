# http://lx.lanqiao.cn/problem.page?gpid=T15


##################################################
# 过 60

n, m = map(int, input().split())
edges = [['a'] * n for _ in range(n)]
for _ in range(m):
    u, v, l = map(int, input().split())
    edges[u - 1][v - 1] = l

visited = {0}
path = [-1] * n
while len(visited) < n:
    shortest, follow = 10001 * n, 0
    for i in range(1, n):
        if edges[0][i] == 'a':
            continue
        if edges[0][i] < shortest and (i not in visited):
            shortest = edges[0][i]
            follow = i
    visited.add(follow)
    path[follow] = shortest

    for i in range(1, n):
        if i not in visited:
            if edges[0][i] == 'a':
                if edges[follow][i] != 'a':
                    edges[0][i] = shortest + edges[follow][i]
            else:
                if edges[follow][i] != 'a':
                    edges[0][i] = min(edges[0][i], shortest + edges[follow][i])

for i in range(1, n):
    print(path[i])

########################################################
# 过 100

from collections import deque, defaultdict

n, m = map(int, input().split())
edges = defaultdict(dict)
for _ in range(m):
    u, v, l = map(int, input().split())
    edges[u - 1][v - 1] = l

visited = {0}
path = [10001 * n] * n
path[0] = 0

q = deque()
q.append(0)
while len(q) > 0:
    p = q.popleft()
    for point in edges[p]:
        if path[point] > path[p] + edges[p][point]:
            path[point] = path[p] + edges[p][point]
            q.append(point)

for i in path[1:]:
    print(i)

###########################################################

'''
https://www.liuchuo.net/archives/7715

#include <iostream>
using namespace std;
int main() {
    int dis[20001] = {0}, u[200001], v[200001],w[200001];
    int n, m, inf = 99999999;
    fill(dis+2,dis+20001,inf);
    scanf("%d %d", &n, &m);
    for(int i = 1;  i <= m; i++)
        scanf("%d %d %d",&u[i], &v[i], &w[i]);
    for(int k = 1; k <= n - 1; k++){
        int  check = 0;
        for(int i = 1; i <= m; i++){
            if(dis[v[i]] > dis[u[i]] + w[i]){
                dis[v[i]] = dis[u[i]] + w[i];
                check = 1;
            }
        }
        if(check == 0) break;
    }
    for(int i = 2; i <= n; i++)
        printf("%d\n",dis[i]);
    return 0;
}
'''


'''
https://blog.csdn.net/Jaster_wisdom/article/details/79522140

#include <iostream>
#include <queue>
#include <vector>
#include <limits.h>
using namespace std;
 
#define INF INT_MAX
int dis[20008];   //起点到各点的最短路径值
bool vis[20008];
queue<int>q;
vector<int> vec[20008];
struct{
    int u,v,s;
}edge[200008];   //只存储边
 
int main(){
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;i++){
        dis[i] = INF;
        vis[i] = 0;
    }
    for(int i=1;i<=m;i++){
        cin>>edge[i].u>>edge[i].v>>edge[i].s;
        vec[edge[i].u].push_back(i);  //把与一点相连的边的序号放在栈中
    }
    dis[1] = 0;
    vis[1] = 1;
    q.push(1);    //先将起点入队
    while(!q.empty()){
        int temp = q.front();  //得到队头元素
        q.pop();         //出队
        vis[temp] = 0;   //出队后立即改变标记
        for(int i=0;i<vec[temp].size();i++){ //遍历顶点1的邻接表
            int k = vec[temp][i];    //表示与temp相连的第k条边
            if(dis[edge[k].v]>dis[temp]+edge[k].s){
                dis[edge[k].v] = dis[temp] + edge[k].s;
                if(!vis[edge[k].v])
                    q.push(edge[k].v);
            }
        }
    }
    for(int i=2;i<=n;i++)
        cout<<dis[i]<<endl;
}
'''