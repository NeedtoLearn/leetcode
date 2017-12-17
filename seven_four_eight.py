class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        shortest_word = ''
        lp_letter_count = self.buildLetterCount(licensePlate.lower())
        for word in words:
            w_letter_count = self.buildLetterCount(word)
            if self.isComplete(lp_letter_count, w_letter_count) and \
                    (not shortest_word or len(word) < len(shortest_word)):
                shortest_word = word
        return shortest_word

    def buildLetterCount(self, s):
        letter_count = {}
        for c in s:
            if c.isalpha():
                letter_count[c] = letter_count.get(c, 0) + 1
        return letter_count

    def isComplete(self, licensePlateLetters, wordLetters):
        for letter in licensePlateLetters:
            if wordLetters.get(letter, 0) < licensePlateLetters[letter]:
                return False
        return True

