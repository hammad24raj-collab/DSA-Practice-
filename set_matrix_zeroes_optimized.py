matrix = [
    [6, 5, 3],
    [3, 3, 5],
    [6, 7, 0]
]

row = len(matrix)
col = len(matrix[0])

first_row_zero = False
first_col_zero = False

# Step 1: check first row
for j in range(col):
    if matrix[0][j] == 0:
        first_row_zero = True

# Step 2: check first column
for i in range(row):
    if matrix[i][0] == 0:
        first_col_zero = True

# Step 3: use first row & col as markers
for i in range(1, row):
    for j in range(1, col):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j] = 0
            
# Step 4: apply markers
for i in range(1, row):
    for j in range(1, col):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0

# Step 5: first row zero
if first_row_zero:
    for j in range(col):
        matrix[0][j] = 0

# Step 6: first column zero
if first_col_zero:
    for i in range(row):
        matrix[i][0] = 0

print(matrix)