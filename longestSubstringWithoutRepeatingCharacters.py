class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set(s)
        sub = set()
        difSub = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in sub:
                    sub.add(s[j])
                else:
                    difSub.append(len(sub))
                    sub = set()
                    break

        if len(unique) == 0 or len(unique) == 1:
            return len(unique)

        return max(difSub)

if __name__ == '__main__':
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))