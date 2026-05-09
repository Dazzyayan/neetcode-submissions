class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            full_product *= num
        
        output = [0] * len(nums)
        for i, num in enumerate(nums):
            if zeros == 1:
                if num == 0:
                    output[i] = int(full_product)
            elif zeros > 1:
                output[i] = 0
            else:
                output[i] = int(full_product/num)

        return output