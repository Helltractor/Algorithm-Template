# Inverse

## Definition

- 单位元：在一个集合中，对于某种运算 （注意：这里代表通用运算的表示符号，并不是特指乘法），如果对于任何的集合元素 ，和元素 运算，得到还是集合元素 本身，则称 为这个运算下的单位元。
- 逆元：在一个集合中，对于某种运算 ，如果任意两个元素的运算结果等于单位元，则称这两个元素互为逆元。
- [费马小定理](https://oi-wiki.org/math/number-theory/fermat/)：若p为素数，gcd(a,p)=1，则有 a <sup>p - 1</sup> ≡ 1 (mod p)。

## Algorithm

### Extended Euclidean Algorithm ([扩展欧几里得算法](https://oi-wiki.org/math/number-theory/inverse/))

```python
# ax + by = gcd(a, b)
def exgcd(a: int, b: int) -> Tuple[int, int]:
    if b == 0:
        return 1, 0
    x, y = exgcd(b, a % b)
    return y, x - a // b * y

# ax ≡ 1 (mod n) -> ax + ny = 1
def inverse(a: int, n: int) -> int:
    x, y = exgcd(a, n)
    return (x % n + n) % n
```

### Linear Congruence Equation ([线性同余方程](https://oi-wiki.org/math/number-theory/linear-equation/))

```python
def exgcd(a: int, b: int, x: int, y: int) -> Tuple[int, int]:
    if b == 0:
        x, y = 1, 0
        return a
    d = exgcd(b, a % b, x, y)
    tmp = x
    x = y
    y = tmp - a // b * y
    return d

# ax ≡ b (mod n)
def linear_congruence(a: int, b: int, c: int, x: int, y: int) -> int:
    d = exgcd(a, b, x, y)
    if c % d:
        return -1
    x *= c // d
    y *= c // d
    return 1
```

### Quick Power (快速幂)

```python
def qpow(x: int, y: int, p: int) -> int:
    res = 1
    while y:
        if y & 1:
            res = res * x % p
        x = x * x % p
        y >>= 1
    return res
```

### Linear inverse (线性求逆)

```python
# 基于费马小定理，只需要p为素数
def inv(a: int, p: int) -> int:
    return qpow(a, p - 2, p)
```

```python
def inverse(n: int, p: int) -> List[int]:
    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (p - p // i) * inv[p % i] % p
    return inv
```
## Links

- [逆元 —— 广义化的倒数](https://zhuanlan.zhihu.com/p/449221995)
- [乘法逆元](https://oi-wiki.org/math/number-theory/inverse/)
- [线性同余方程](https://oi-wiki.org/math/number-theory/linear-equation/)
- [扩展欧几里得算法](https://oi-wiki.org/math/number-theory/exgcd/)
- [欧拉定理 & 费马小定理](https://oi-wiki.org/math/number-theory/fermat/)