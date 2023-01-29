def convert(s: str, numRows: int):
        rows = [''] * numRows
        k = 0
        direction = (numRows == 1) - 1
        for char in s:
            rows[k] += char
            if k == 0 or k == numRows - 1:
                direction *= -1
            k += direction
        return ''.join(rows)
s = "PAYPALISHIRING"
numRows = 3
print(convert(s,numRows))