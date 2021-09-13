'''
找寻英文句子中单词包含x为后缀的单词首个字母位置
时间限制： 3000MS
内存限制： 589824KB
题目描述：
给定英文句子S和字符串x，判断x是否为S中某些单词的后缀，若匹配到则输出所有匹配单词的位置，否则输出-1。
例如：输入"this is an easy problem."和"is"，输出[0,5]
例如：输入"In love folly is always sweet"和"an"，输出[]
例如：输入"Whatever is worth doing is worth doing well."和"well"，输出[39]
输入描述
输入包含两行，第一行为S，第二行为x
长度不超过10000
输出描述
int型数组
样例输入
No one and you.
""
样例输出
[]
提示
因为给定的是英语句子，所以输入中可能存在标点符号
'''


def func(S, x):
    res = []
    str_arr = S.strip(',').strip('.').split()
    for i in range(0, len(str_arr)):
        if str_arr[i].endswith(x):
            res.append(i + 1)
    return res


while True:
    try:
        S = str(input())
        x = str(input())
        print(func(S, x))
    except:
        break

'''
感觉给的示例有问题
'''