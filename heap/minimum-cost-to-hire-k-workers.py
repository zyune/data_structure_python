from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], K: int
    ) -> float:
        effs = [(q / w, q) for q, w in zip(quality, wage)]
        print(effs)
        effs.sort(key=lambda a: -a[0])
        ans = float("inf")
        print(effs)
        h = []
        total = 0
        for rate, q in effs:
            heapq.heappush(h, -q)  # 这是个最大堆
            total += q
            if len(h) > K:
                total += heapq.heappop(h)
            if len(h) == K:
                ans = min(ans, total / rate)
        return ans


quality = [3, 1, 10, 10, 1]
wage = [4, 8, 2, 2, 7]
k = 3

# quality = [10, 20, 5]
# wage = [70, 50, 30]
# k = 2
solution = Solution()
print(solution.mincostToHireWorkers(quality, wage, k))

