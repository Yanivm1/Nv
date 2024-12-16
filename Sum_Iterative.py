def Two_in_Arr_equal_X(arr, X):
    len1 = len(arr)
    if len1 < 2:  # wrong input protection
        return False

    for i in range(len1-1):
        for num in arr[i + 1:]:
            if arr[i] + num == X:
                return True
    return False


# Executing the function
arr = [4, 2, 5, 7, 9]  # Provided array
X = 15  # Requested sum

Answer = Two_in_Arr_equal_X(arr, X)

print(f"Are there two elements in array {arr} that sum {X}? -> {Answer}")


