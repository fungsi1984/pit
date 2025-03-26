class Solution:
	def minOperations(self, grid: list[list[int]], x: int) -> int:
		arr = sorted([a for row in grid for a in row])
		if any((a - arr[0]) % x for a in arr):
			return -1

		ans = 0

		for a in arr:
			ans += abs(a - arr[len(arr) // 2]) // x

		return ans


# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4

solution = Solution()
grid = [[2, 4], [6, 8]]
x = 2

print(solution.minOperations(grid, x))
