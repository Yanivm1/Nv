def stairs(N):
    if N < 0:
        return 'bad input'
    if 1 <= N <= 3:
        return N

    # the result is always the sum of 2 previous values
    counter = [1, 2]  # initializing the counter
    for i in range(3, N):  # alternating in order to keep the last two
        if i % 2 != 0:  # odd number
            counter[0] = counter[0] + counter[1]
        else:  # even number
            counter[1] = counter[0] + counter[1]

    return counter[0]+counter[1]


# Executing the function
N = 4  # number of stairs

print(f"The number of combinations to climb stairs in steps of 1 or 2 in case of {N} stairs is {stairs(N)}")




