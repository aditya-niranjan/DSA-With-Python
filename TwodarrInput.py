
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))



values = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter the value for row {i}, column {j}: "))
        row.append(value)
    values.append(row)

print("2D array input complete.")

print(values)