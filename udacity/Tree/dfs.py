

def pre_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):

        if node:
            #visit
            visit_order.append(node.get_value())
            #traverse left
            traverse(node.get_left_child())
            #traverse right
            traverse(node.get_right_child())

    traverse(root)

    return visit_order


# define in-order traversal
def in_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):

        if node:
            #visit
            #traverse left
            traverse(node.get_left_child())
            visit_order.append(node.get_value())

            #traverse right
            traverse(node.get_right_child())

    traverse(root)

    return visit_order


# define post_order traversal
def post_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):

        if node:
            #visit
            #traverse left
            traverse(node.get_left_child())

            #traverse right
            traverse(node.get_right_child())

            visit_order.append(node.get_value())

    traverse(root)

    return visit_order





## Using stack.

class Stack():
    def __init__(self):
        self.list = list()

    def push(self,value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"

class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s



def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while(node):
        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
        count +=1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    if debug_mode:
        print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
    return visit_order

