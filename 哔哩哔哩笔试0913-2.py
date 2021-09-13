'''
乘积差最大值寻找
时间限制： 3000MS
内存限制： 589824KB
题目描述：
两个数对 (a, b) 和 (c, d) 之间的 乘积差 定义为 (a * b) - (c * d) 。 例如，(5, 6) 和 (2, 7) 之间的乘积差是 (5 * 6) - (2 * 7) = 16 。
给你一个整数数组 nums ，选出四个不同的下标 w、x、y 和 z ，使数对 (nums[w], nums[x]) 和 (nums[y], nums[z]) 之间的 乘积差取到最大值 。 返回以这种方式取得的乘积差中的最大值 。 示例 ： 输入：nums = [4,2,5,9,7,4,8] 输出：64
解释：可以选出下标为 3 和 6 的元素构成第一个数对 (9, 8) 以及下标 1 和 5 构成第二个数对 (2, 4) 乘积差是 (9 * 8) - (2 * 4) = 64
输入描述
int型数组
注意，输入格式请严格参照“输入样例”
输出描述
int
样例输入
[4,2,5,9,7,4,8]
样例输出
64
'''


def func(nums):
    nums.sort()
    return nums[-1] * nums[-2] - nums[0] * nums[1]


while True:
    try:
        # nums = str(input())
        # nums = nums.strip('[').strip(']').split(',')
        # nums = list(map(int, nums))
        nums = list(map(int, input()[1:-1].split(',')))
        print(func(nums))
    except:
        break
