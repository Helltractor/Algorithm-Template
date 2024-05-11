from typing import List


def plusOne(digits: List[int]) -> List[int]:
    n, temp, res = len(digits), 0, []
    for i in range(n):
        temp *= 10
        temp += digits[i]
    temp += 1
    for i in range(n + 1):
        res.append(temp % 10)
        temp //= 10
    if res[n - 1]:
        return res[n - 1::-1]
    else:
        return res[::-1]


if __name__ == '__main__':
    digits = [6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]
    print(plusOne(digits))
