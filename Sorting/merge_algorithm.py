def merge_alg(arr):
    def merge(arr, l, m, r)
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]

        # Initial indexes for left, right, and merged array
        i = j = 0
        k = l

        # Merge the temp arrays back into arr[l:r+1]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy the remaining elements of left[], if there are any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy the remaining elements of right[], if there are any
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def merge_fun(arr, l, r):
        if l < r:
            m = (l + r) // 2
            merge_fun(arr, l, m)  # Sort the first half
            merge_fun(arr, m + 1, r)  # Sort the second half
            merge(arr, l, m, r)  # Merge the sorted halves

    # Call merge_fun with the initial parameters
    merge_fun(arr, 0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    sorted_arr = merge_alg([10, 5, 30, 15, 7])
    print(sorted_arr)
