class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i = 0
        # j = 1
        # k = len(nums) - 1
        nums.sort()
        triplets = []

        for i in range(0, len(nums), 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # print("i", i)
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                # print("sum", sum)
                if sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        
        return triplets