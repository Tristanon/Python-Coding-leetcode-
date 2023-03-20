#930.Binary_Subarrays_With_Sum.py
# Solution 1
class Solution:
	def numSubarraysWithSum(self, A: List[int], S: int) -> int:
		d = collections.defaultdict(int)
		d[0] = 1
		cur_sum = 0
		res = 0
		for i in A:
			cur_sum += i
			if cur_sum - S in d:
				res += d[cur_sum - S]
			d[cur_sum] += 1
		return res