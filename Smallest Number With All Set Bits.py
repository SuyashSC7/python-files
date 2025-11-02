def smallestnumber(n: int):
    i = n
    while True:
        nby = bin(i)[2:]      # convert to binary string
        if '0' not in nby:    # if all bits are 1
            return i          # found the answer
        i += 1                # move to next number
print(smallestnumber(10))