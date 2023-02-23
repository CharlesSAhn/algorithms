



'''

API

'''

from collections import deque

class Friends():

    def __init__(self):
        self.graph = {}  #  { "user1" : ["user2", ....]



    def friendCheckBFS(self, user1, user2):

        queue = deque([user1])
        visit = set([user1])

        while queue:

            person = queue.popleft()

            for friend in self.graph[person]:

                if friend is user2:
                    return True

                if person not in visit:
                    visit.add(friend)
                    queue.append(friend)

        return False





    def friendsCheck(self, user1, user2):

        visit = set()

        def dfs(node):

            for friend in self.graph[node]:

                if friend == user2:
                    return

                if friend not in visit:
                    visit.add(friend)
                    dfs(friend)
            return False

        return dfs(user1)


    def backtrack(self, user1, user2):

        visit = set()
        output = [user1]
        res = []

        def dfs(node):

            for friend in self.graph[node]:
                if friend == user2:
                    output.append(friend)
                    res = output[:]
                    return

                if friend not in visit:
                    visit.add(friend)
                    output.append(friend)
                    dfs(friend)
                    output.pop()
            return False

        dfs(user1)
        return res




        if user2 in self.graph[user1]:
            return True


