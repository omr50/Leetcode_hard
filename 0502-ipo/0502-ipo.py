from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_to_profit = defaultdict(list) 

        # we need to include value in hashmap as a list because even though it seems to make sense to
        # take only the top one, what if the business ventures down the line that require more capital
        # still have less profit, so its best to include everything to be safe. The heap will do the
        # rest.

        # get a list of all the profits per capital  
        for i in range(len(capital)):
            capital_to_profit[capital[i]].append(profits[i])
        

        # start at total profit = 0
        curr_profit = w
        heap = []
        min_heap = [(c, p) for c, p in zip(capital, profits)]

        heapify(min_heap)
        for i in range(k):

            # BIG LOGIC FLAW: the issue with looping from the previous profit to the current one
            # is that you basically waste so many iterations. Now imagine if there is only one item
            # within that range, and the jump has a difference of 1 million. Now you just wasted 1 million
            # iterations for one jump. So instead use a min heap to feed the max heap. Or you can sort the
            # input array and basically keep a pointer from the start range to the end range.

            # for j in range(prev_profit, curr_profit + 1): 
            #     for profit in capital_to_profit[j]:
            #         heappush(heap, -profit)
            if not len(min_heap):
                if not len(heap):
                    return curr_profit

            while len(min_heap) and min_heap[0][0] <= curr_profit:
                heappush(heap, (-1 * heappop(min_heap)[1]))  
        
            if not len(heap):
                return curr_profit
            curr_profit += (-1 * heappop(heap))
        
        return curr_profit
        
        