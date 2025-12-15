from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count0 = students.count(0)
        count1 = students.count(1)

        for s in sandwiches:
            if s == 0:
                if count0 == 0:
                    return count1
                count0 -= 1
            else:
                if count1 == 0:
                    return count0
                count1 -= 1

        return 0
sol = Solution()
print(sol.countStudents([1,1,0,0], [0,1,0,1]))