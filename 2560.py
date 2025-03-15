import bisect

class Solution:
    def numStolenHouses(self, capacity: int) -> int:
        stolenHouses = 0
        i = 0
        while i < len(self.nums):
            if self.nums[i] <= capacity:
                stolenHouses += 1
                i += 1  # Skip the next house
            i += 1
        return stolenHouses

    def minCapability(self, nums: list[int], k: int) -> int:
        self.nums = nums  # Store nums as an instance variable
        return bisect.bisect_left(range(max(nums) + 1), k, key=self.numStolenHouses)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [2, 3, 5, 9]
    k1 = 2
    print(solution.minCapability(nums1, k1))  # Output: 5

    # Example 2
    nums2 = [2, 7, 9, 3, 1]
    k2 = 2
    print(solution.minCapability(nums2, k2))  # Output: 2
