from typing import List


def compress(chars: List[str]) -> int:
    n = len(chars)
    if n == 1:
        return n
    left, right = 0, 1
    res = []
    while right <= n:
        while right < n and chars[left] == chars[right]:
            right += 1
        res.append(chars[left])
        if right - left > 1:
            res += list(str(right - left))
        left = right
        right += 1
    chars[:] = res[:]
    return len(chars)


def compress1(chars: List[str]) -> int:
    n = len(chars)
    if n == 1: return n
    write, left, right = 0, 0, 1
    while right <= n:
        chars[write] = chars[left]
        write += 1
        while right < n and chars[left] == chars[right]: right += 1
        if right - left > 1:
            temp = list(str(right - left))
            chars[write:write + len(temp)] = temp[:]
            write += len(temp)
        left = right
        right += 1
    return write


if __name__ == '__main__':
    chars = ["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b",
             "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c",
             "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]
    chars1 = ["a", "b", "c"]
    print(chars[:compress1(chars)])
    print(chars1[:compress1(chars1)])
