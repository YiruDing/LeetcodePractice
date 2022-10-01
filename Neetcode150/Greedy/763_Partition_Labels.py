class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}

        for i, c in enumerate(s):
            lastIdx[c] = i
            # get/update the lastIndex of each letter

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIdx[c])

            if i == end:
                res.append(size)
                size = 0


# Set the size back to 0 so we can append the size of each part
# No need to update the end so we can keep on track if i ==end.
        return res
