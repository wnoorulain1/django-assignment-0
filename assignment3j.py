#Given an array heights that contains the height of each bar in the histogram, and we are asked to return the area of the largest rectangle in the histogram. Note that eachbar has a width of 1 heights| ≥ 1 heights [i] ≥ 0

def largest_rectangle_area(heights):
    stack = []  # stores indices of bars
    max_area = 0
    heights.append(0)  # Sentinel to pop all bars at the end

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            # If stack is empty, width is i
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    heights.pop()  # Remove the sentinel
    return max_area


# Example usage:
heights = [2, 1, 5, 6, 2, 3]
print(largest_rectangle_area(heights))  # Output: 10