from typing import List


class Solution:
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        lx, rx, uy, dy = 0, m - 1, 0, n - 1
        x, y, cnt = 0, 0, 0
        ret = []
        while cnt < m * n:
            while x <= rx and cnt < m * n:
                ret.append(matrix[y][x])
                cnt += 1
                x += 1
            uy += 1
            x, y = rx, uy
            while y <= dy and cnt < m * n:
                ret.append(matrix[y][x])
                cnt += 1
                y += 1
            rx -= 1
            x, y = rx, dy
            while x >= lx and cnt < m * n:
                ret.append(matrix[y][x])
                cnt += 1
                x -= 1
            dy -= 1
            x, y = lx, dy
            while y >= uy and cnt < m * n:
                ret.append(matrix[y][x])
                cnt += 1
                y -= 1
            lx += 1
            x, y = lx, uy
        return ret


if __name__ == '__main__':
    matrix = [[[1, 11], [2, 0], [3, 13], [0, 14], [5, 0], [6, 16], [0, 0], [8, 18], [9, 19], [10, 20]],
              [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
              ]
    print(Solution.spiralOrder(matrix[0]))
    print([1, 11, 0, 13, 14, 0, 16, 0, 18, 19, 20, 10, 9, 8, 0, 6, 5, 0, 3, 2])
    print(Solution.spiralOrder(matrix[1]))
    print([1, 2, 3, 6, 9, 8, 7, 4, 5])
    print(Solution.spiralOrder(matrix[2]))
    print([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
