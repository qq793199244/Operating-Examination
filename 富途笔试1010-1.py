'''
最大值
'''


class Solution:
    def solve(self, nums):
        n = len(nums)
        nums = list(map(str, nums))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if int(nums[i] + nums[j]) <= int(nums[j] + nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        while nums and nums[0] == '0':
            nums.pop(0)
        return ''.join(nums) if nums else '0'


if __name__ == '__main__':
    u = Solution()
    print(u.solve([30, 1]))  # 301
    print(u.solve([2, 20, 23, 4, 8]))  # 8423220
    print(u.solve([2]))  # 2
    print(u.solve([10]))  # 10
    print(u.solve([0, 0, 10, 20]))  # 201000
