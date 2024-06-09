class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        pre_row = [poured]
        
        for row in range(1, query_row + 1):
            cur_row = [0] * (row + 1)
            for i in range(row):
                extra_champ = pre_row[i] - 1
                if extra_champ > 0:
                    cur_row[i] += (extra_champ / 2)
                    cur_row[i + 1] += (extra_champ / 2)
            pre_row = cur_row
        
        
        return min(1, pre_row[query_glass])