from typing import List

class Solution:
    # memory efficient


    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     length = len(nums)
    #     for idx1 in range(length):
    #         for idx2 in range(idx1+1, length):
    #             if nums[idx1]+nums[idx2]==target:
    #                 return [idx1, idx2]



    # runtime efficient

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for idx, num in enumerate(nums):
            nums_dict.setdefault(num,[]).append(idx)
            # nums_dict[num] = idx
        for num in nums:
            if num!=target-num and nums_dict.get(target-num):
                return [nums_dict[num][0], nums_dict[target-num][0]]
            elif  nums_dict.get(target-num) and len(nums_dict[target-num])>1:
                return [nums_dict[num][0], nums_dict[num][1]]
