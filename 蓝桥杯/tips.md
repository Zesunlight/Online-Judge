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

### 算法

- BFS，定义一个类表示每一个点，类里可以用一个属性存储当前步数；或者使用队列的时候，pop原队列，新节点push到新队列，原队列空了，令原队列等于新队列，步数加一
- 二分法，求XX最大值最小是多少、XX最小值最大是多少
- 用二进制来压缩01数组，便于集合去重

### 数学

- $$
  \vec{a}=\left(x_{1}, y_{1}\right), \quad \vec{b}=\left(x_{2}, y_{2}\right) \\
  \vec{a} \cdot \vec{b}=|\vec{a}| \cdot|\vec{b}| \cdot \cos <\vec{a}, \vec{b}> = x_{1} x_{2} + y_{1} y_{2} \\
  |\vec{a} \times \vec{b}|=|\vec{a}| \cdot|\vec{b}| \cdot \sin <\vec{a}, \vec{b}> = |x_{1} y_{2}-x_{2} y_{1}|
  $$

- 叉积可用于计算多边形面积

- $$
  \vec{a} \times \vec{b} = 
  \left|\begin{array}{ccc}
  i & j & k \\
  a x & a y & a z \\
  b x & b y & b z
  \end{array}\right|
  $$

- 

