'''

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.


Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

input:  prerequisites = [[1,2],[2,3],[3,7],[7,1], [1,5]
{
1: 2,
2: 3,
7: 1
}
does cycle exists?

'''
from collections import defaultdict


class GraphNode():

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_children(self, node):

        self.children.append(node)



def buildGraph(preRequiresites):

    courses = {}

    for sublist in preRequiresites:

        i_value = sublist[0]
        j_value = sublist[1]

        if i_value not in courses:
            courses[i_value] = GraphNode(i_value)

        if j_value not in courses:
            courses[j_value] = GraphNode(j_value)

        courses[i_value].add_children( courses[j_value])

    return courses




def canFinish(numCourses, preRequiresites):


    if len(preRequiresites) == 0:
        return True


    graph = defaultdict(list)


    for course, prereq in preRequiresites:

        graph[course].append(prereq)


    def fn(node):


        if node not in seen:
            seen.add(node)
            for kid in graph[node]:
                res = fn(kid)
                if res is False:
                    return False
            fin.add(node)
            seen.remove(node)
        else:
            return False


    seen, fin = set(), set()

    for node in graph.copy():
        if node not in seen:
            res = fn(node)
            if res is False:
                return False

    return len(fin) >= numCourses


print(canFinish(4,   [[1,2],[2,3],[3,7], [7,1]]))
print(canFinish(4,   [[1,0],[0,1]]))
print(canFinish(4,[[1,4],[2,4],[3,1],[3,2]]))









