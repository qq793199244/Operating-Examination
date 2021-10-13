'''
凑总金额
时间限制： 5000MS
内存限制： 589824KB
题目描述：
给定不同面额的纸币 moneys 和一个总金额 total。编写一个函数来计算可以凑成总金额所需的最少的纸币张数。
如果没有任何一种组合能组成总金额，返回 -1。 每种纸币的数量是无限的。 输入 [1, 2, 5] , 11 输出 3 （11 = 5 + 5 + 1） 输入 [2], 3 输出-1 (无解)     int change(vector<int>& moneys, int total) {     }

输入描述
不同面额的纸币moneys：int数组类型
总金额 total：int
输出描述
所需的最少纸币张数
样例输入
[1, 2, 5]
11
样例输出
3
提示
注意：输入包含[ ]  ；数字间有英文逗号和一个空格
同LeetCode322零钱兑换
'''
def change(moneys, total):
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in moneys:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == '__main__':
    moneys = str(input())
    total = int(input())
    moneys = list(map(int, moneys[1:-1].split(',')))
    print(change(moneys, total))