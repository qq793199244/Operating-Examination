'''
二叉树查找
时间限制： 3000MS
内存限制： 589824KB
题目描述：
已知二叉搜索树如下所示(根节点 记为root) ：
给定一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
备注：异常情况，输出-1
输入描述
整数k：int类型
k≤100
输出描述
第k个最小元素：int类型
样例输入
5
样例输出
12
'''


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


root = TreeNode(10)
n6 = root.left = TreeNode(6)
n1 = n6.left = TreeNode(1)
n8 = n6.right = TreeNode(8)
n15 = root.right = TreeNode(15)
n13 = n15.left = TreeNode(13)
n18 = n15.right = TreeNode(18)
n12 = n13.left = TreeNode(12)
n14 = n13.right = TreeNode(14)
n17 = n18.left = TreeNode(17)
n19 = n18.right = TreeNode(19)


def kthSmallest(root, k):
    if k <= 0 or k > 11:
        return -1
    res = []
    stack = [root]
    while len(stack):
        top = stack.pop()
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)
        res.append(top.val)
    res.sort()
    return res[k - 1]


while True:
    try:
        k = int(input())
        print(kthSmallest(root, k))
    except:
        break
