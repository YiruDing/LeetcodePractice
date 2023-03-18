

# StefanPochmann
def minimumTotal(self, t):
    return reduce(lambda a, b: [f + min(d, e) for d, e, f in zip(a, a[1:], b)],
                  t[::-1])[0]


# Explanation
# Starting with the bottom row, I move upwards, always combining the current row and the next upper row. At the end, I have combined everything into the top row and simply return its only element. Here's a longer version with meaningful variable names:


def minimumTotal(self, triangle):

    def combine_rows(lower_row, upper_row):
        return [
            upper + min(lower_left, lower_right) for upper, lower_left,
            lower_right in zip(upper_row, lower_row, lower_row[1:])
        ]
        # zip
        # https://www.programiz.com/python-programming/methods/built-in/zip

    return reduce(combine_rows, triangle[::-1])[0]