def ex():
    i = 0
    j = 5
    x = 0
    count = 0
    while (j > i):        # loop while i < 5
        if (i == 7):      # this condition will never be True (since loop ends before i reaches 7)
            break
        x = x + i + count
        count = count + 2
        i = i + 1
    print(f"Value of x: {x} count: {count} j: {j} x: {x}")

if __name__ == "__main__":
    ex()
