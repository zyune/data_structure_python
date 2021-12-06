from typing import List
import heapq

# 解题思路 其实这道题不就是让我们选 k 个人，工作效率比取他们中最低的，并按照这个最低的工作效率计算总工资，找出最低的总工资么


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
        for (
            rate,
            q,
        ) in (
            effs
        ):  # effs has been sorted so the q/w of every element after is smaller than the previous one
            heapq.heappush(h, -q)  # 这是个最大堆，开始push的时候 value是依据 quality 来判断的 为什么？
            total += q
            if len(h) > K:
                total += heapq.heappop(
                    h
                )  # 每次 pop出去的还是q最大的 ，q是整个total / rate的分子 分子越小 值越小
            if len(h) == K:
                ans = min(ans, total / rate)
        return ans


# quality = [3, 1, 10, 10, 1]
# wage = [4, 8, 2, 2, 7]
# k = 3

quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
solution = Solution()
print(solution.mincostToHireWorkers(quality, wage, k))

