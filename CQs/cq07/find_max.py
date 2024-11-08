def find_and_remove_max(nums: list[int]) -> int:
    index: int = 0
    if len(nums) == 0:  # if list is empty it returns -1 as max
        max = -1
    else:
        max: int = nums[0]
        for i in nums:
            if max < i:
                max = i
    while index < len(nums):  # goes through the list to remove max
        if nums[index] == max:
            nums.pop(index)
        index += 1
    return max
