matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered_1 = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]
filtered_2 = [[x for x in row if (x % 3 == 0)] for row in matrix if sum(row) >= 10]
#filtered_3 = [[x for x in row (if x % 3 == 0)] for row in matrix if sum(row) >= 10]

print(filtered_1)
print(filtered_2)
