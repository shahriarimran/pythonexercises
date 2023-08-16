#no of rows
i =3
#no of columns
j = 4

rows, cols = (i, j)
arr = [[0 for cols in range(j)] for rows in range(i)]

for rows in range(i):
    for cols in range(j):
        arr[rows][cols]= rows*cols
print(arr)