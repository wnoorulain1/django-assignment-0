#Given an integer n, generate all the valid combinations of n pairs of parentheses

def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        # If the current string is complete
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Add "(" if we still have open brackets left
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        
        # Add ")" if closing brackets are fewer than opening
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


# Example usage:
n = 3
print(generate_parentheses(n))
# Output: ['((()))', '(()())', '(())()', '()(())', '()()()']