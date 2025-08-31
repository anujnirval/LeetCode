class Solution:
    def twoSum(self, nums, target):
        index1 = 0;
        index2 = 0;
        result = []
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    index1 = i
                    index2 = j
                j += 1

        result.append(index1)
        result.append(index2)
        return result

if __name__ == '__main__':
    nums = [2,7,11,11]
    target = 9

    solution = Solution()
    print(solution.twoSum(nums, target))