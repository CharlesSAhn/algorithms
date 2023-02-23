'''
Define the print function for the Tree class. Nodes on the same level are printed on the same line.

For example, the tree we've been using would print out like this:

Node(apple)
Node(banana) | Node(cherry)
Node(dates) | <empty> | <empty> | <empty>
<empty> | <empty>
We'll have <empty> be placeholders so that we can keep track of which node is a child or parent of the other nodes.

hint: use a variable to keep track of which level each node is on. For instance, the root node is on level 0, and its child nodes are on level 1.

'''


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    """
    define the print function
    """
    def __repr__(self):
        # queue
        level = 0
        q = Queue()
        # visit order
        visit_order = list()
        #start at root
        node = self.get_root()
        #add root to queue
        q.enq((node, level))

        #while queue is not empty:
        while len(q) > 0:
            node, level = q.deq()

            if node == None:
                visit_order.append( ("<Empty>", level) )
                continue
            visit_order.append( (node, level) )

            if node.has_left_child():
                q.enq( (node.get_left_child(), level + 1) )
            else:
                q.enq( (None, level+1) )
            if node.has_right_child():
                q.enq( (node.get_right_child(), level + 1) )
            else:
                q.enq( (None, level+1) )

        s = "Tree\n"
        previous_level = -1

        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level
        return s