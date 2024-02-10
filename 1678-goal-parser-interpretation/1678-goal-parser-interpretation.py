class Solution(object):
    def interpret(self, command):
        
        answer = []
        
        for idx,com in enumerate(command):
            if com == 'G':
                answer.append('G')
            elif com == '(':
                if command[idx + 1] == ')':
                    answer.append('o')
                else:
                    answer.append('al')
        
        return "".join(answer)
        