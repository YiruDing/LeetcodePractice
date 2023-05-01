class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        left, right = 0, len(people) - 1

        while left <= right:
            remain = limit - people[right]
            right -= 1
            res += 1
            if remain >= people[left] and left <= right:
                left += 1
        return res