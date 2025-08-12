#With the range of numbers from 1 to n inclusive, we can make n! permutations. By labeling them in order starting from 1, you are asked to return the kth permutation

def get_permutation(n, k):
    from math import factorial

    nums = list(range(1, n + 1))  # Numbers to permute
    k -= 1  # Convert to zero-based index
    result = []

    for i in range(n, 0, -1):
        fact = factorial(i - 1)
        index = k // fact
        result.append(str(nums.pop(index)))
        k %= fact

    return "".join(result)


# Example usage:
n = 3
k = 3
print(get_permutation(n, k))  