### 输入

- `n = int(input().strip())`
- `a, b = map(float, input().strip().split())`
- `data = map(int, input().strip().split())`
  `n, array = data[0], data[1:]`

### 输出

![format](format.png)

- `print(f'{1.1006:.3f}')`  `1.101`
- `print(f'{1.1004:.3f}')`  `1.100`
- `print(f'{4*5/2:.0f}')`  `10` （输出时注意除法，会有小数产生）
- `print(f'{65:c}')`  `A` （ASCII码）

### 技巧

- 多用 `math.pow(a, n)`
- `n & 1 == 0` 是否偶数
- `mid = left + ((right - left) >> 1)` 二分法取中点
- 题目中说 多少多少的倍数、结果取模，在计算过程中即可取模，不必等到最终结果
- `sys.maxsize` `float('inf')` 最大值
- `bisect.bisect_left(*a*, *x*, *lo=0*, *hi=len(a)*)` 二分查找

### 算法

- BFS，定义一个类表示每一个点，类里可以用一个属性存储当前步数；或者使用队列的时候，pop原队列，新节点push到新队列，原队列空了，令原队列等于新队列，步数加一
- 二分法，求XX最大值最小是多少、XX最小值最大是多少
- 用二进制来压缩01数组，便于集合去重
- `itertools.accumulate(nums)` 前缀和
- 差分 $b_{i}=\left\{\begin{array}{ll}
  a_{i}-a_{i-1} & i \in[2, n] \\
  a_{1} & i=1
  \end{array}\right.$

#### 格雷码

- 格雷码是一个二进制数系，其中两个相邻数的二进制位只有一位不同。

-  k 位的格雷码可以从  k-1 位的格雷码以上下镜射后加上新位的方式快速的得到
  $$
  \begin{matrix} k=1\\ 0\\ 1\\\\\\\\\\\\\\ \end{matrix} \to \begin{matrix}\\ \color{Red}0\\\color{Red}1\\\color{Blue}1\\\color{Blue}0\\\\\\\\\\ \end{matrix} \to \begin{matrix} k=2\\ {\color{Red}0}0\\{\color{Red}0}1\\{\color{Blue}1}1\\{\color{Blue}1}0\\\\\\\\\\ \end{matrix} \to \begin{matrix}\\ \color{Red}00\\\color{Red}01\\\color{Red}11\\\color{Red}10\\\color{Blue}10\\\color{Blue}11\\\color{Blue}01\\\color{Blue}00 \end{matrix} \to \begin{matrix} k=3\\ {\color{Red}0}00\\{\color{Red}0}01\\{\color{Red}0}11\\{\color{Red}0}10\\{\color{Blue}1}10\\{\color{Blue}1}11\\{\color{Blue}1}01\\{\color{Blue}1}00 \end{matrix}
  $$

- `int g(int n) { return n ^ (n >> 1); }` 

  $G(n)=n\oplus \left\lfloor\frac{n}{2}\right\rfloor$ 

#### 双向广搜的步骤

```
将开始结点和目标结点加入队列 q
标记开始结点为 1
标记目标结点为 2
while (队列 q 不为空)
{
  从 q.front() 扩展出新的 s 个结点

  如果 新扩展出的结点已经被其他数字标记过
    那么 表示搜索的两端碰撞
    那么 循环结束

  如果 新的 s 个结点是从开始结点扩展来的
    那么 将这个 s 个结点标记为 1 并且入队 q 

  如果 新的 s 个结点是从目标结点扩展来的
    那么 将这个 s 个结点标记为 2 并且入队 q
}
```



### 数学

$$
\vec{a}=\left(x_{1}, y_{1}\right), \quad \vec{b}=\left(x_{2}, y_{2}\right) \\
  \vec{a} \cdot \vec{b}=|\vec{a}| \cdot|\vec{b}| \cdot \cos <\vec{a}, \vec{b}> = x_{1} x_{2} + y_{1} y_{2} \\
  |\vec{a} \times \vec{b}|=|\vec{a}| \cdot|\vec{b}| \cdot \sin <\vec{a}, \vec{b}> = |x_{1} y_{2}-x_{2} y_{1}| \\
  \vec{a} \times \vec{b} = 
\left|\begin{array}{ccc}
  i & j & k \\
  a x & a y & a z \\
  b x & b y & b z
  \end{array}\right|
$$

- 叉积可用于计算多边形面积

- 若要求反正切函数，尽量使用 `atan2(y, x)`，用途比 `atan(x)` 广泛

- Pick 定理：给定顶点均为整点的简单多边形，皮克定理说明了其面积 $A$ 和内部格点数目 $i$  、边上格点数目  $b$ 的关系：$A=i+\frac{b}{2}-1$。

- 以整点为顶点的线段，覆盖的点的个数为 $\gcd(dx, dy)$  ，其中 $dx,dy$ 分别为线段横向占的点数和纵向占的点数，其中一个为 0 时需特殊处理。

- 

