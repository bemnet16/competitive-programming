class Solution:
    def smallestNumber(self, num: int) -> int:
        
        # if it is 0 return 0
        if num == 0: return num
        
        # conver the number to string to traverse it
        # append non-zero digits to nums 
        # append '0's to zeros list
        n_str = str(num)
        nums = []
        zeros = []
        
        for n in n_str:
            # handle the negative numbers /discard '-' sign if the number is less than 0 /
            if n != "0" and n != "-":
                nums.append(n)
            elif n == "0":
                zeros.append(n)
                
                
        # if num is less than 0 sort the digits in descending order to be the minimum number
        if num < 0:
            
            nums.sort(reverse = True)
            answer = nums + zeros
            
            # conver the final number to negative
            return 0 - int("".join(answer))
            
          
        # if num is positive only the first non-zero minmum digit must proceed the zeros
        else:
            
            nums.sort()
            answer = nums[:1] + zeros + nums[1:]
            
            return int("".join(answer))
        
        
        
            
        
        
        