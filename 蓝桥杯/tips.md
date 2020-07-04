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
- 