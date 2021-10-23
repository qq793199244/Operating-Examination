'''
统计字符串s中的小写字母出现次数，用哈希表显示
'''
def func(s):
    if not s:
        return {}
    hash_table = {}
    for c in s:
        if c.islower():
            hash_table[c] = hash_table.get(c, 0) + 1
    return hash_table

if __name__ == '__main__':
    print(func(''))
    print(func('AAABBBaaabbc'))
    print(func('123abcdefg'))
    print(func('ABCD'))