from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]

    res = [[1], [1, 1]]

    for i in range(2, numRows):
        row = [1]

        for j in range(len(res[i-1]) - 1):
            row.append(res[i - 1][j] + res[i - 1][j + 1])

        row.append(1)
        res.append(row)

    return res

if __name__ == '__main__':
    numRows = 5
    res = generate(5)
    assert len(res) == numRows
