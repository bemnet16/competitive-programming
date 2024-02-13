class Solution:
    def numberOfWays(self, s: str) -> int:
        # compute the prefix sum of '0's and '1's
        prefix_one = []
        prefix_zero = []

        sum_one = 0
        sum_zero = 0

        for i in range(len(s)):

            if s[i] == '0':
                sum_zero += 1
            else:
                sum_one += 1

            prefix_one.append(sum_one)
            prefix_zero.append(sum_zero)    


        answer = 0
        for i in range(len(s)):

            if s[i] == '0':
                left_ones = prefix_one[i]
                right_ones = prefix_one[-1] - prefix_one[i]
                num_ways = left_ones * right_ones
                answer += num_ways
            
            else:
                left_zeros = prefix_zero[i]
                right_zeros = prefix_zero[-1] - prefix_zero[i]
                num_ways = left_zeros * right_zeros
                answer += num_ways
        
        return answer
        