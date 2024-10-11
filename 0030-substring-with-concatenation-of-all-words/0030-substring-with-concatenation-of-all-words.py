class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # working?
        word_size = len(words[0])
        word_hashmap = {}
        window_length = word_size * len(words)
        for word in words:
            if word in word_hashmap:
                word_hashmap[word] += 1
            else:
                word_hashmap[word] = 1

        # loop over all indexes to create array of words
        # loop over all indexes.
        # for each index check if a word exists, then check the
        # word len index away from it and check if that exists.
        # then basically gather until we have all words.

        # we need array to hold all the possible words based on word len
        # also 2 pointers that will be word len apart to capture all words
        # avoid edge cases by handling them now

        if len(s) < word_size:
            return []
        l, r = 0, word_size - 1

        
        # now we have all words and each one starts from its corresponding starting char index in the array
        # O(n) loop multiplied by the operations inside (yet to determine)
        output = []
        # print(word_array)
        for i in range(len(s) - window_length +1):
            # o(words length) operation each time
            temp_hashmap = {}
            remaining_words = len(words)
            # if the remaining words will hit 0 then we have reached the solution
            j = i
            while j < i + window_length:
                curr_word = s[j: j + word_size]
                if curr_word not in word_hashmap:
                    break
                temp_hashmap[curr_word] = 1 + temp_hashmap.get(curr_word, 0)
                if temp_hashmap[curr_word] > word_hashmap[curr_word]:
                    break
                remaining_words -= 1
                j += word_size
                if remaining_words == 0:
                    output.append(i)
                    break
        return output