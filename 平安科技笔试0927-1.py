'''
给你两个二进制字符串，返回它们的和（用二进制表示）
'''


class Solution:
    def addBinary(self, a, b):
        a = int(a, 2)
        b = int(b, 2)
        return bin(a+b)[2:]


if __name__ == '__main__':
    u = Solution()
    print(u.addBinary('11', '1'))  # '100'
    print(u.addBinary('1010', '1011'))  # '10101'
