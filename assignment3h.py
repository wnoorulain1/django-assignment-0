#With the range of numbers from 1 to n inclusive, we can make n! permutations. By labeling them in order
#starting from 1, you are asked to return the kth permutation


from math import factorial

def get_permutation(n, k):
    numbers = list(range(1, n + 1))  # List of available numbers
    k -= 1  # Convert k to zero-based index
    result = []

    for i in range(n, 0, -1):
        fact = factorial(i - 1)
        index = k // fact
        result.append(str(numbers.pop(index)))
        k %= fact

    return "".join(result)


# Example usage:
n = 4
k = 9
print(get_permutation(n, k)) 