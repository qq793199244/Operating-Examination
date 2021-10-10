'''
数组中两个字符串的最小距离
'''


class Solution:
    def minDistance(self, strs, str1, str2):
        # write code here
        if not str1 or not str2:
            return -1
        if str1 not in strs or str2 not in strs:
            return -1
        if str1 == str2:
            return 0
        dis, min_dis = 1, len(strs)
        pos1, pos2 = 0, len(strs)
        for i in range(len(strs)):
            if strs[i] == str1:
                pos1 = i
                for j in range(len(strs)):
                    if strs[j] == str2:
                        pos2 = j
                dis = abs(pos1 - pos2)
                if dis < min_dis:
                    min_dis = dis
        return min_dis


if __name__ == '__main__':
    u = Solution()
    print(u.minDistance(['CD'], 'CD', 'AB'))  # -1
    print(u.minDistance(['QWER', '1234', 'qwe', '666', 'QWER'], 'QWER', '666'))  # 1
