import random
import unittest
from collections import Counter


class MyTestCase(unittest.TestCase):
    def test_something(self):
        
        def check(n):
            cnt = sorted([(k, v) for k, v in Counter(n).items()], key=lambda x: (-x[1], x[0]))
            cnt_ = ''.join([k for k, v in cnt])
            s = {k: len(cnt_) - i - 1 for i, k in enumerate(cnt_)}
            ans = []
            for i, c in enumerate(n):
                ans.append(cnt_[s[c]])
            return ''.join(ans)
        while True:
            tmp = ''
            for i in range(100):
                j = random.randint(0, 26)
                tmp += chr(ord('a') + j)
                s = check(tmp)
                if check(s) != tmp:
                    print(tmp)
                    break
                    

if __name__ == '__main__':
    unittest.main()
