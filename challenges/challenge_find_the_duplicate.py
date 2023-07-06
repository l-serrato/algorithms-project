def find_duplicate(nums):
    if not nums or isinstance(nums, str) or len(nums) == len(set(nums)):
        return False

    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

    return False
