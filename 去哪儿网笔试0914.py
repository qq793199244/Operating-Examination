'''
给定一个字符串，找到第一个不重复的字符，并返回该字符的索引。如果不存在，则返回-1
假定该字符串只包含小写字母。
输入描述
footballgamefinal
输出描述
3
输入描述
loveleetcode
输出描述
2
'''
def func(s):
    if not s:
        return -1
    n = len(s)
    for i in range(n):
        if s[i] not in s[i+1:] and s[i] not in s[:i]:
            return i
    return -1

def func2(s):
    dic = {}
    for c in s:
        dic[c] = dic.get(c, 0) + 1
    for i, c in enumerate(s):
        if dic[c] == 1:
            return i
    return -1

while True:
    try:
        s = str(input())
        print(func2(s))
    except:
        break