def Two_in_Arr_equal_X(arr1, X, Orig_last_item):
    # print(arr1) # showing the recursion flow
    if len(arr1) < 2:  # stop case 1 and protection from bad input
        return False
    elif len(arr1) == 2:  # stop case 2 - when there are only 2 elements left at the array
        return arr1[0] + arr1[1] == X

    else:
        # 3 parts for calculating the results:
        #   1. Checking sum of first+last items of current array.
        #   2. Recursion-1: remove the last item of the array for next iteration.
        #   3. Recursion-2: remove the first item of the array, 'preparing' new array for elements 1 and 2.
        return (
                arr1[0] + arr1[-1] == X  # part 1
                or (Two_in_Arr_equal_X(arr1[:-1], X, Orig_last_item))  # part 2
                or (Two_in_Arr_equal_X(arr1[1:], X, Orig_last_item) if arr1[-1] == Orig_last_item else False)  # part 3
        )


# Executing the function
arr1 = [13,0,4,6,15]  # Provided array
Orig_last_item = arr1[-1]  # keeping the value of last item from the provided array
X = 4  # Requested sum


Answer = Two_in_Arr_equal_X(arr1, X, Orig_last_item)

print(f"Does array {arr1} has a combination equals to {X} ? -> {Answer}")

