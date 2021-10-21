'''
质数对
给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。
如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10，分别为(5,5),(3,7)）
输入描述:
输入包括一个整数n,(3 ≤ n < 1000)
输出描述:
输出对数
输入例子:
10
输出例子:
2
'''


class Solution:
    def CountPrime(self, num: int) -> int:
        # write code here
        if num < 2:
            return 0
        res = []
        for i in range(2, num):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                res.append(i)
        n = len(res)
        count = 0
        left, right = 0, n - 1
        while left <= right:
            if res[left] + res[right] == num and left <= right:
                count += 1
                left += 1
                right -= 1
            elif res[left] + res[right] > num and left <= right:
                right -= 1
            else:
                left += 1
        return count


if __name__ == '__main__':
    u = Solution()
    print(u.CountPrime(10))
