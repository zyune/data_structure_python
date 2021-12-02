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


# heapify make an min heap defaultly
# looking for a keth largest is actually using a min heap other node values are all bigger than the root,then the root is the kthe largest
# on the other hand. if we are looking for the kth smallest value, we are gonna use a max heap. other node values are all smaller than the root, then the root is the kth smallest
# what most important matter is the root!!!

nums = [3, 2, 1, 5, 6, 4]
k = 2
aaa = Solution()
print(aaa.findKthLargest(nums, k))

heap = [x for x in nums[:k]]
print(heap)
heapq.heapify(heap)

