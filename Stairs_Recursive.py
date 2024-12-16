def stairs(N, counter):
    if N == 0 or N == 1:  # stop case - finish climb of specific unique combination
        counter[0] += 1  # counting the combinations
        # print(counter) # showing the counter increment
        return

    else:
        stairs(N - 1, counter)  # next step - 1 stair
        stairs(N - 2, counter)  # next step - 2 stairs


# Executing the function
N = 6  # number of stairs
counter = [0]  # reset counter

stairs(N, counter)

print(f"The number of combinations to climb stairs in steps of 1 or 2 in case of {N} stairs is {counter[0]}")

