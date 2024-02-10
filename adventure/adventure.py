
def quick_sort(arr):
    """
    Sorts a list in ascending order using the quicksort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [4, 2, 7, 10, 9, 5, 3]
sorted_arr = quick_sort(arr)
print(sorted_arr)
