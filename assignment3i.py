#Given two strings s and t, find the shortest substring of s that contains all characters of t

from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)
    required = len(t_count)  # unique characters needed

    left = 0
    formed = 0
    window_counts = {}
    min_len = float("inf")
    min_window_str = ""

    for right, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        # Try to shrink the window from the left
        while left <= right and formed == required:
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                min_window_str = s[left:right+1]

            # Remove leftmost character
            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                formed -= 1
            left += 1

    return min_window_str


# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t)) 