class Solution(object):
    def dailyTemperatures(self, temperatures):

        tempt = [0] * len(temperatures)
        tem_li = []

        for repo, value in enumerate(temperatures):
            if len(tem_li) == 0:
                tem_li.append((value,repo))
                continue
            while len(tem_li) != 0 and tem_li[len(tem_li) - 1][0] < value:
                popped_temp = tem_li.pop()
                tempt[popped_temp[1]] = repo - popped_temp[1]
            tem_li.append((value,repo))

        return tempt
