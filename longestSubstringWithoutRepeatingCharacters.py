from operator import index


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set(s)
        sub = []
        difSub = []
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in sub:
                    sub.append(s[j])
                else:
                    difSub.append(sub)
                    sub=[]
                    break


        if len(unique) == 0 or len(unique) == 1:
            return len(unique)

        difSub.sort(key=len,reverse=True)
        return len(difSub[0])

if __name__ == '__main__':
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))