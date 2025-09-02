class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        maxLen = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in sub:
                    sub.add(s[j])
                else:
                    if len(sub) > maxLen:
                        maxLen = len(sub)
                    sub = set()
                    break
        maxLen = max(maxLen, len(sub))
        sub = set()

        return maxLen


if __name__ == '__main__':
    s = " "
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))