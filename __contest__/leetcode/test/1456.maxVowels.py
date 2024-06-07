class Solution:
    '''
    def maxVowels(s: str, k: int) -> int:
        temp = 'aeiou'
        n = len(s)
        right = 0
        ret = ans = 0
        while right < n:
            while right < k:
                if s[right] in temp:
                    ret += 1
                    ans = ret
                right += 1
            if s[right] in temp and s[right - k] not in temp:
                ret += 1
            elif s[right] not in temp and s[right - k] in temp:
                ret -= 1
            ans = max(ans, ret)
            right += 1
        return ans
    '''

    def maxVowels1(s: str, k: int) -> int:
        temp = 'aeiou'
        right = ret = 0
        print(len(s))
        for ch in s[:k]:
            if ch in temp:
                ret += 1
        print(ret)
        to_ret = ret
        while right < len(s) - k:
            if s[right] in temp:
                ret -= 1
            if s[right + k] in temp:
                ret += 1
            to_ret = max(to_ret, ret)
            right += 1
        return to_ret


if __name__ == '__main__':
    s = "weallloveyou"
    s1 = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
    k = 7
    k1 = 33
    print(Solution.maxVowels(s, k))
