'''
给定一个字符串，其中仅包含：大小写字母，数字和问号。要求对该字符串内部字符排序，满足以下条件：
1. 问号的占用的位置不变
2. 数字占用的位置不变，数字之间由大到小排序
3. 字母占用的位置不变，字母之间按字典序排序
输入描述：
一个字符串，只包含：大小写字母，数字，问号
输出描述：
按规则排序后的字符串
示例1：
输入：12A?zc
输出：21A?cz

示例2：
输入：1Ad?z?t24
输出：4Ad?t?z21

示例3：
输入：???123??zxy?
输出：???321??xyz?
'''


def func(s):
    if not s:
        return s
    n = len(s)
    res = []
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num_stack = []
    s_stack = []
    for c in s:
        if c in nums:
            num_stack.append(c)
        elif c == '?':
            continue
        else:
            s_stack.append(c)
    num_stack.sort(reverse=True)
    s_stack.sort()
    for i in range(n):
        if s[i] in nums:
            res.append(num_stack.pop(0))
        elif s[i] == '?':
            res.append('?')
        else:
            res.append(s_stack.pop(0))
    return ''.join(res)


if __name__ == '__main__':
    print(func('12A?zc'))  # 21A?cz
    print(func('1Ad?z?t24'))  # 4Ad?t?z21
    print(func('???123??zxy?'))  # ???321??xyz?
