#Given an array of integers arr and an integer k, find the kth largest element

#1 ≤k≤|arr|

import heapq

def kth_largest(arr, k):
    # heapq.nlargest returns the k largest elements in descending order
    return heapq.nlargest(k, arr)[-1]

# Example usage
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(arr, k))

