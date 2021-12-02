from typing import List
import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        dummy = ListNode(0)
        p = dummy
        head = []  # head 就是我们 sort所用到的那个heap，哟共有几个listnode， head中就有几个element
        for i in range(len(lists)):
            if lists[i]:  # i就是一个指针，所指向的对象就是 在大list 中的listnode
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
                # According to the example from the documentation,
                # you can use tuples, and it will sort by the first element of the tuple:
        while head:  # 如果堆里还有元素 就要继续排
            val, idx = heapq.heappop(
                head
            )  # 推出最小的 哪个被pop出来 一会push 也push这个指针对应的listnode 的next的值
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:  # 如果idx所指向的listnode 还不是null，也就是还没遍历完
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


a1 = ListNode(1)
a2 = ListNode(4)
a3 = ListNode(5)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

c1 = ListNode(2)
c2 = ListNode(6)

c1.next = c2

lists = [a1, b1, c1]
Solution1 = Solution()
result = Solution1.mergeKLists(lists)

while result:
    print(result.val)
    result = result.next

