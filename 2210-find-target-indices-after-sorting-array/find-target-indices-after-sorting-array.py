class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        sorted_list = sorted(nums)
        empty_list = []
        for i, num in enumerate(sorted_list):
            if num == target:
                empty_list.append(i) 
    
        return empty_list

