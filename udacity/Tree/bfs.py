from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"



# BFS algorithm
def bfs(tree):
    # queue
    q = Queue()
    # visit order
    visit_order = list()
    #start at root
    node = tree.get_root()
    #add root to queue
    q.enq(node)

    #while queue is not empty:
    while len(q) > 0:
        node = q.deq()
        visit_order.append(node)

        if node.has_left_child():
            q.enq(node.get_left_child())
        if node.has_right_child():
            q.enq(node.get_right_child())

    return visit_order