class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        cur_idx = 0
        word = ''
        stack = []
        for c in S:
            if c.isalpha():
                word += c
                cur_idx += 1
                if cur_idx == K:
                    return c
            else:
                if word:
                    stack.append(word)
                stack.append(c)
                word = ''
                cur_idx = cur_idx * int(c)
                if cur_idx >= K:
                    while stack:
                        if stack[-1].isalpha():
                            if K > cur_idx - len(stack[-1]):
                                return stack[-1][K - (cur_idx - len(stack[-1])) - 1]
                            cur_idx -= len(stack[-1])
                        else:
                            cur_idx /= int(stack[-1])
                            K = K % cur_idx
                            if K == 0:
                                for s in stack[::-1]:
                                    if s.isalpha():
                                        return s[-1]
                        stack = stack[:-1]

