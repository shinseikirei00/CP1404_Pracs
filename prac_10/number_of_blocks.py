def number_of_blocks(row):
    if row <=0:
        return 0
    # else:
    #     blocks += row
    #     number_of_blocks(row-1,blocks)
    return row + number_of_blocks(row - 1)


number_of_rows= int(input("How many rows? "))
# number_of_blocks(number_of_rows, 0)

print("{} rows needs {} blocks".format(number_of_rows, number_of_blocks(number_of_rows)))