'''
根据偏移量原地旋转字符串
'''


class Solution:
    def rotateCharArrayInPlace(self, arr, offset):
        n = len(arr)
        offset = offset % n
        arr[:] = arr[n - offset:] + arr[:n - offset]
        return arr


if __name__ == '__main__':
    u = Solution()
    print(u.rotateCharArrayInPlace(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 3))  # ['e', 'f', 'g', 'a', 'b', 'c', 'd']
    print(u.rotateCharArrayInPlace(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 0))  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(u.rotateCharArrayInPlace(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 1))  # ['g', 'a', 'b', 'c', 'd', 'e', 'f']
    print(u.rotateCharArrayInPlace(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 10))  # ['e', 'f', 'g', 'a', 'b', 'c', 'd']
