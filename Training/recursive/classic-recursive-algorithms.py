from typing import List

def sum_array(nums: List[int], count: int) -> List[int]:
    if count == 0:
        return 0
    return sum_array(nums, count-1) + nums[count-1]


nums = [1, 2, 3, 4]
result = sum_array(nums, len(nums))
print(f"A soma é {result}")


