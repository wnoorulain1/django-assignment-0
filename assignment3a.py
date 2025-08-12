#Given a sorted array of integers arr and an integer target, find the index of the first and last position of target in arr. In target can't be found in arr, return [-1, - 1

def find_first_and_last(arr, target):
    def find_bound(is_first):
        left, right = 0, len(arr) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1  # search on left side
                else:
                    left = mid + 1   # search on right side
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    first = find_bound(True)
    last = find_bound(False)
    return [first, last]


# Example usage:
arr = [5, 7, 7, 8, 8, 10]
target = 8
print(find_first_and_last(arr, target))  # Output: [3, 4]