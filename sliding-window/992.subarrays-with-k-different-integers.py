class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.num_nonzero = 0

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.num_nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.num_nonzero -= 1


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Window()
        window2 = Window()

        ans = l1 = l2 = 0

        for r, x in enumerate(A):
            window1.add(x)
            window2.add(x)

            while window1.num_nonzero > K:
                window1.remove(A[l1])
                l1 += 1

            while window2.num_nonzero >= K:
                window2.remove(A[l2])
                l2 += 1

            ans += l2 - l1

        return ans
