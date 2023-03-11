# We can count the gap only.But how?
# Hashmap!
# key:position value: count of the gap
# rows - the position with max gaps


class Solution:

    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0: 0}
        # mapping posotion:count of brick gaps
        # 加這個，是要確保其非empty

        for row in wall:
            total = 0
            for brick in row[:-1]:
                # 3/10 不可include the most right gap
                total += brick
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())