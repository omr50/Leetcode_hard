from collections import defaultdict
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        char_suffix = defaultdict(set)
        for idea in ideas:
            char_suffix[idea[0]].add(idea[1:])
        
        res = 0
        # 26 x 26 loop
        # inner might be n in total across all iterations
        # because for each character in the 26, there could be
        # from 0 to n suffixes in there. So therefore all iterations
        # should sum up to n. Since we are doing char 1, and char 2
        # its then 26x26xn so its really O(n) time.
        for ch1 in char_suffix:
            for ch2 in char_suffix:
                if ch1 == ch2:
                    # continue since it won't work if both chars are same
                    continue
                intersect = 0 
                suffix2_map = char_suffix[ch2]
                for suffix in char_suffix[ch1]:
                    if suffix in  suffix2_map:
                        intersect +=1
                distinct1 = len(char_suffix[ch1]) - intersect
                distinct2 = len(char_suffix[ch2]) - intersect
                res += (distinct1*distinct2) 
        return res







        