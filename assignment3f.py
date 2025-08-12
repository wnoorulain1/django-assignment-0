#Given an integer n representing the number of courses (courses are labeled from 0 ton - 1), and an array prerequisites where prerequisites[i] = [a, b] means that you first need to take the course b before taking the course a, determine if it's possible to finish all the courses

from collections import defaultdict, deque

def can_finish(num_courses, prerequisites):
    # Build graph and indegree array
    graph = defaultdict(list)
    indegree = [0] * num_courses
    
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    
    # Start with courses having no prerequisites
    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    taken_courses = 0
    
    while queue:
        course = queue.popleft()
        taken_courses += 1
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    # If we have taken all courses, it's possible
    return taken_courses == num_courses


# Example usage:
n = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]
print(can_finish(n, prerequisites))  # Output: True

prerequisites2 = [[1, 0], [0, 1]]
print(can_finish(n, prerequisites2))  # Output: False