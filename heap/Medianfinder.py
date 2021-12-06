class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return -self.max_heap[0]


# In a normal base case , the num should enter into the max heap. unless it is bigger than the max heap
# the smallest number in minheap is bigger than the root of the max heap

# 建立一个大顶堆，并存放最小的 $(n + 1) \div 2$ 个数，这样堆顶的数就是第 $(n + 1) \div 2$ 小的数，也就是奇数情况的中位数。
# 建立一个小顶堆，并存放最大的 n - $(n + 1) \div 2$ 个数，这样堆顶的数就是第 n - $(n + 1) \div 2$ 大的数，结合上面的大顶堆，可求出偶数情况的中位数。
# 有了这样一个知识，剩下的只是如何维护两个堆的大小了。
# 如果大顶堆的个数比小顶堆少，那么就将小顶堆中最小的转移到大顶堆。而由于小顶堆维护的是最大的 k 个数，大顶堆维护的是最小的 k 个数，因此小顶堆堆顶一定大于等于大顶堆堆顶，并且这两个堆顶是此时的中位数。
# 如果大顶堆的个数比小顶堆的个数多 2，那么就将大顶堆中最大的转移到小顶堆，理由同上。
