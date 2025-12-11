def Reversearray(arr):
    i, j = 0, len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = Reversearray(numbers)
print(result)