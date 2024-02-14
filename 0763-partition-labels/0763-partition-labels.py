class Solution:
    def partitionLabels(self, start_inde: str) -> List[int]:
        
        # track the start and end index of all characters
        track_start_end = {}

        for i in range(len(start_inde)):

            cur_value = start_inde[i]
            
            # if already exist update its end index
            if cur_value in track_start_end:
                track_start_end[cur_value][1] = i

            else:
                track_start_end[cur_value] = [i,i]
                
        # sort the start with end index value by there start index to easly merge them
        track_list = sorted(track_start_end.values(), key = lambda x:x[0])
        
        # start form the first partion by using the start and end index of the first character
        partition_stat = track_list[0][0]
        partition_end = track_list[0][1]

        answer = []
        
        for start_inde,end_index in track_list:
            
            if start_inde > partition_end:
                answer.append(partition_end - partition_stat + 1)
                partition_stat = start_inde
                partition_end = end_index

            elif end_index > partition_end:
                partition_end = end_index
        
        # append the remaining final partition
        answer.append(partition_end - partition_stat + 1)
        
        return answer