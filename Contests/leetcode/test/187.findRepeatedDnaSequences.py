from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    temp = set()
    res = []
    n = len(s)
    print(n)
    if n < 10: return res
    for i in range(n - 9):
        ch = s[i:i + 10]
        if ch not in temp:
            temp.add(ch)
        else:
            if ch not in res:
                res.append(ch)
    return res


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    s1 = "AAAAAAAAAAAAA"
    s2 = "AAAAAAAAAAA"
    print(findRepeatedDnaSequences(s2))
