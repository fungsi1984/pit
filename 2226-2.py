class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        l = 1
        r = sum(candies) // k

        while l < r:
            m = (l + r) // 2
            if self.numChildren(candies, m) < k:
                r = m
            else:
                l = m + 1

        return l if self.numChildren(candies, l) >= k else l - 1

    def numChildren(self, candies: list[int], m: int) -> int:
        return sum(c // m for c in candies)


# Example usage
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Example 1
    candies1 = [5, 8, 6]
    k1 = 3
    result1 = solution.maximumCandies(candies1, k1)
    print(f"Maximum candies per child for {candies1} with {k1} children: {result1}")
    # Expected output: 5 (each child can get 5 candies)

    # Example 2
    candies2 = [2, 5]
    k2 = 11
    result2 = solution.maximumCandies(candies2, k2)
    print(f"Maximum candies per child for {candies2} with {k2} children: {result2}")
    # Expected output: 0 (not enough candies to distribute)

    # Example 3
    candies3 = [4, 7, 9]
    k3 = 4
    result3 = solution.maximumCandies(candies3, k3)
    print(f"Maximum candies per child for {candies3} with {k3} children: {result3}")
    # Expected output: 3 (each child can get 3 candies)
