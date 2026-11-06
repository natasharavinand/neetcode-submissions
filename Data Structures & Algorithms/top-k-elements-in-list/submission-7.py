class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]

        for num in counter:
            buckets[counter[num]].append(num)
        
        result = []

        count = 0
        idx = len(buckets) - 1

        while count < k:
            j = 0
            while j < len(buckets[idx]) and count < k:
                result.append(buckets[idx][j])
                count += 1
                j += 1
            idx -= 1
        
        return result
        
        

