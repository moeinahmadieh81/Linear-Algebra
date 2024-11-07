import numpy as np

print("Please enter the rows of your matrix:")
rows = int(input())
print("Please enter the columns of your matrix:")
cols = int(input())
arr = []
print("Enter each entry in one line:")

# For user input
for i in range(rows):  # A for loop for row entries
    a = []
    for j in range(cols):  # A for loop for column entries
        a.append(float(input()))
    arr.append(a)
arr = np.array(arr, dtype=float)
r = arr.shape[0]
c = arr.shape[1]
curr_row = 0
curr_col = 0
pivot_rows = []
pivot_cols = []
while curr_row < r and curr_col < c:
    is_zero = 1
    while is_zero == 1:
        for i in range(curr_row, r):
            if arr[i][curr_col] != 0:
                is_zero = 0
        if is_zero == 1:
            curr_col += 1
        if curr_col == c:
            break
    if curr_col == c:
        break
    for i in range(curr_row, r):
        if arr[i][curr_col] != 0:
            arr[[curr_row, i]] = arr[[i, curr_row]]
            break
    for i in range(curr_row + 1, r):
        if arr[i][curr_col] != 0:
            arr[i] -= (arr[i][curr_col] / arr[curr_row][curr_col]) * arr[curr_row]
    pivot_rows.append(curr_row)
    pivot_cols.append(curr_col)
    curr_row += 1
    arr = np.around(arr, decimals=8)
echelon = arr
print('\nEchelon Form:\n', echelon)
reduced = echelon.copy()
pivot_cols.reverse()
pivot_rows.reverse()
for i in range(len(pivot_cols)):
    reduced[pivot_rows[i]] /= (reduced[pivot_rows[i]][pivot_cols[i]])
    for j in range(pivot_rows[i]):
        reduced[j] -= (reduced[j][pivot_cols[i]] / reduced[pivot_rows[i]][pivot_cols[i]]) * reduced[pivot_rows[i]]
print('\nReduced Echelon Form:\n', reduced)
print("Answers of Matrix:")

for i in range(len(reduced) - 1, -1, -1):
    sum = 0
    found1 = False
    for j in range(0, len(reduced[0]) - 1):
        if reduced[i][j] == 1:
            found1 = True
            for k in range(j + 1, len(reduced[0]) - 1):
                sum += 10 * reduced[i][k]
            break
    if not found1 and reduced[i][-1] != 0:
        print("system is inconsistent because")
        print(reduced[i])
        exit(0)

    if not found1 and reduced[i][-1] == 0:
        print('x ' + str(j + 1) + ' is free variable' )

    else:
        answer = reduced[i][-1] - sum
        print('x ' + str(j + 1) + ' is ' + str(answer))

