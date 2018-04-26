class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Create set of substrings of original words
        sub_words = set()
        for word in words:
            for i in range(1, len(word)):
                sub_words.add(word[-i:])
        # Filter word which exists in sub_words
        words = set([word for word in words if word not in sub_words])
        # Compute the length of encoded string
        return sum([len(word) for word in words]) + len(words)
