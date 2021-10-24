'''

'''
def func(arr1, arr2):
    m, n = len(arr1), len(arr2)
    if m > n:
        arr1, arr2 = arr2, arr1
    res = []
    for num in arr1:
        if num in arr2:
            res.append(num)
    return res

if __name__ == '__main__':
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    res = func(arr1, arr2)
    for i in res:
        print(i)