class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for letter in s:
            if not stack:
                stack.append(letter)
                continue
            if letter == 'B' and stack[-1]=='A':
                stack.pop()
            elif letter =='D' and stack[-1]=='C':
                stack.pop()
            else:
                stack.append(letter)
        return len(stack)

class Solution:
    def minLength(self, s: str) -> int:
        s = list(s)
        top = -1
        for i in range(len(s)):
            if top >= 0 and s[top] + s[i] in ("AB","CD"):
                top -= 1
            else:
                top += 1
                s[top] = s[i]
        return top + 1
