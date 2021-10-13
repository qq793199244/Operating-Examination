'''
排序链表删除重复元素
时间限制： 3000MS
内存限制： 589824KB
题目描述：
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。 示例 1: 输入: 1->1->2 输出: 1->2 示例 2: 输入: 1->1->2->3->3 输出: 1->2->3
输入描述
排序链表
输出描述
排序链表且没有重复元素
样例输入
1->1->2->3->3
样例输出
1->2->3
'''
def func(s):
    if not s:
        return s
    s = s.split('->')
    n = len(s)
    res = [s[0]]
    for i in range(1, n):
        if s[i] in res:
            continue
        else:
            res.append(s[i])
    return '->'.join(res)

if __name__ == '__main__':
    s = str(input())
    print(func(s))