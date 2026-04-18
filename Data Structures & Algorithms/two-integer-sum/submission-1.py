class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {} #map value:index

        for i in range(len(nums)):
            ht[nums[i]] = i

        for i in range(len(nums)):
            other = target - nums[i]

            if other in ht:
                if ht[other]!=i:
                    first = min(i,ht[other])
                    second = max(i,ht[other])
                    return [first,second]

        