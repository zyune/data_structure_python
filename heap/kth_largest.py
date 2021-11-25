import heapq


class Solution(object):
    def findKthLargest(self, nums, k) -> int:
        #   构造大小为 k 的小顶堆
        heap = [x for x in nums[:k]]
        heapq.heapify(heap)
        n = len(nums)
        for i in range(k, n):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
aaa = Solution()
print(aaa.findKthLargest(nums, k))

heap = [x for x in nums[:k]]
heapq.heapify(heap)
print(heap)
for i in range(5):
    print(i)
