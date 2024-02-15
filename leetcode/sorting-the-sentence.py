class Solution(object):
    def sortSentence(self, s):

        #Check length constriants
        if len(s) < 2 or len(s) > 200:
            return "The sentence length shoud be between 2 and 200"

        sen = []
        for i in s.split():
            sen.append(i[-1] + i[:len(i) - 1])

        for i in range(len(sen)):
            for j in range((i + 1),len(sen)):
                if sen[i][0] > sen[j][0]:
                    sen[i], sen[j] = sen[j], sen[i]
            sen[i] = sen[i][1:]

        return(" ".join(sen))



