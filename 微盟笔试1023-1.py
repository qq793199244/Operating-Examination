'''

'''


# def func(s):
#     nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     res = []
#     for c in s:
#         if c in nums:
#             res.append(c)
#     return ''.join(res)

def func(s):
    res = ''
    for c in s:
        if c.isdigit():
            res += c
    return res


if __name__ == "__main__":
    s = str(input())
    print(func(s))
