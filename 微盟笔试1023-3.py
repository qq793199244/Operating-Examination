'''

'''
def func(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1

while True:
    try:
        nums = list(map(int, input().split()))
        target = int(input())
        print(func(nums, target))
    except:
        break