class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        if nums[i] == target: return i
        if nums[j] == target: return j
        while target > nums[i] and target < nums[j]:
            mid = i + (j - i) // 2
            if mid == i:
                break
            if nums[mid] > target:
                j = mid
            elif nums[mid] < target:
                i = mid
            else:
                return mid

        for z in range(i, j + 1, 1):
            if nums[z] > target:
                return -1
            elif nums[z] == target:
                return z

        return -1