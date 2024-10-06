class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        num_open = 0
        for ch in s:
            if ch == '(':
                stack.append('(')
                num_open += 1
            else:
                if num_open > 0:
                    acc = 0
                    while stack and stack[-1] != '(':
                        acc += stack[-1] 
                        stack.pop()
                    if stack[-1] == '(':
                        num_open -= 1
                        stack.pop()
                    stack.append(acc + 2)

                else:
                    stack.append(')')


        max_counter, curr = 0, 0
        for ch in stack:
            if ch not in ['(', ')']:
                curr += ch
            else:
                curr = 0
            max_counter = max(max_counter, curr)
        
        return max_counter


       
        # I think the solution here won't work because there is
        # a constant set of state that needs to be held for each
        # possible sub solution. And so recursion might fit well
        # here to be able to model that instead of the commented out solution below it
        # the solution commented out doesn't work particularly because we
        # cannot know the longest_sequence as we go since that is dependent
        # on counting out all valid parenthesis. So we need to basically
        # go through the whole thing, determine if it is all inter-connected
        # or if there are some gaps, and basically find the biggest connected
        # part.

        # Naively one would think to look at all possible substrings and then
        # determine if they are valid, and their size. Then get the largest
        # valid one. Since we know how to determine if valid and determine
        # size, this should be relatively easy. But every substring would
        # be a lot of work.

        # To make it easier you can do every substring starting with an open
        # bracket. But still in worst case you would be analyzing every index.


        # The main thing I'm having an issue on is like in the example below:
        # "(()(((()"

        # In this test case the issue is the disconnected part. So we have one opening
        # and closing pair in the beginning. ANd one closing and opening pair in the end.
        # This example doesn't show the case I want exactly but it does remind me of it.

        # for a case where there is one opening and closing and then a long list of opening
        # then evenly matching closings. The issue is that the total would be all of those
        # plus the first 2. And there could be several move patterns like this, and even more
        # so, one big open close wrapping all of those up. So keeping track of those feels like
        # having to keep track of a stack, or of a state of a json parser or something of the sort.

        # Maybe if I keep track of indexes.

        # for this example:
        # "(()(((()"

        # [0, 2, 0, 0, 0, 2, 0]
        # If there are indexes that are consecutive then we can combine totals

        # (()(((()))))

        # the array cannot be built immediately though.


        # this leads me to thinking that this is too complex of an approach

        # the classic stack setup may help more.
        







        # longest_sequence, curr_sequence = 0, 0
        # opening_count = 0
        # previous_sequence = []
        # for ch in s:
        #     if ch == ')': 
        #         if opening_count:
        #             if opening_count == 1:
        #                 prev = 0
        #                 if previous_sequence:
        #                     prev = previous_sequence[-1]
        #                     previous_sequence.pop()

        #                 curr_sequence += 2 + prev 
        #                 previous_sequence.append(curr_sequence)
        #                 longest_sequence = max(sum(previous_sequence), longest_sequence)
        #                 curr_sequence = 0
        #             else:
        #                 previous_sequence.append(2)
        #                 longest_sequence = max(2, longest_sequence)

        #             opening_count -= 1
        #         else:
        #             longest_sequence = max(longest_sequence, sum(previous_sequence))
        #             curr_sequence = 0
        #             opening_count = 0
        #             previous_sequence = []
        #     elif ch == '(':
        #         opening_count += 1
            
        # print(previous_sequence)
        # if len(previous_sequence):
        #     longest_sequence = max(longest_sequence, previous_sequence[-1])
        # return longest_sequence 



# "(()(((()"
# "(()(((()"
# "()(())"


