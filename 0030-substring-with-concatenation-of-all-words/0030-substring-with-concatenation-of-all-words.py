class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []
        
        word_freq = {}
        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)
        
        word_len = len(words[0])
        window_len = len(words) * word_len

        res = []

        for i in range(len(s) - window_len + 1):
            substr_freq = {}
            j = i

            while j < i + window_len:
                cur_word = s[j:j+word_len]

                if cur_word not in word_freq:
                    break
                substr_freq[cur_word] = substr_freq.get(cur_word, 0) + 1

                if substr_freq[cur_word] > word_freq[cur_word]:
                    break
                j += word_len
            
            if j == i + window_len:
                res.append(i)
        
        return res
        # word_size = len(words[0])
        # word_hashmap = {}

        # for word in words:
        #     if word in word_hashmap:
        #         word_hashmap[word] += 1
        #     else:
        #         word_hashmap[word] = 1




        # # loop over all indexes to create array of words
        # # loop over all indexes.
        # # for each index check if a word exists, then check the
        # # word len index away from it and check if that exists.
        # # then basically gather until we have all words.

        # # we need array to hold all the possible words based on word len
        # # also 2 pointers that will be word len apart to capture all words
        # # avoid edge cases by handling them now

        # if len(s) < word_size:
        #     return []
        # l, r = 0, word_size - 1

        # word_array = []
        
        # # create word array
        # while r < len(s):
        #     word = ""
        #     for i in range(l, r + 1):
        #         word += s[i]
        #     word_array.append(word)

        #     l += 1
        #     r += 1
        
        # # now we have all words and each one starts from its corresponding starting char index in the array
        # # O(n) loop multiplied by the operations inside (yet to determine)
        # output = []
        # # print(word_array)
        # for i in range(len(s)):
        #     # o(words length) operation each time
        #     temp_hashmap = {}
        #     remaining_words = len(words)
        #     # if the remaining words will hit 0 then we have reached the solution
        #     j = i
        #     word_counter = 0
        #     while j < len(word_array): 
        #         curr_word = word_array[j]
        #         if curr_word in word_hashmap and (curr_word not in temp_hashmap or word_hashmap[curr_word] - temp_hashmap[curr_word] > 0):
        #             remaining_words -= 1
        #             temp_hashmap[curr_word] = 1 + temp_hashmap.get(curr_word, 0)
        #             j += word_size
        #             word_counter += 1
        #         else:
        #             break
        #         if word_counter == len(words):
        #             break
        #     if remaining_words == 0:
        #         output.append(i)
            
        # return output






