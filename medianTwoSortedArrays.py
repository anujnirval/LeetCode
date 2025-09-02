class Solution:
    def __init__(self,nums1,nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    def findMedianSortedArrays(self) -> float:
        finalArray = nums1 + nums2
        finalArray.sort()
        if len(finalArray)%2 ==0:
            return (finalArray[(len(finalArray)//2)] + finalArray[(len(finalArray)//2)-1])/2
        else:
            return finalArray[len(finalArray)//2]

if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3,4]
    solution = Solution(nums1,nums2)
    print(solution.findMedianSortedArrays())