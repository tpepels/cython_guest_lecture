import cython
import math
import random

@cython.cclass
class Node:
    state: cython.int
    parent: cython.pointer(Node)
    children: list
    visits: cython.int
    value: cython.double

    def __init__(self, state: cython.int, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0

    @cython.ccall
    def is_fully_expanded(self) -> cython.bint:
        return len(self.children) > 0

    @cython.ccall
    def best_child(self, exploration_weight: cython.double = 1.414):
        best_score: cython.double = -float('inf')
        best_child: cython.pointer(Node) = None

        for child in self.children:
            exploitation = child.value / child.visits
            exploration = exploration_weight * math.sqrt(math.log(self.visits) / child.visits)
            score = exploitation + exploration
            if score > best_score:
                best_score = score
                best_child = child

        return best_child

    @cython.ccall
    def expand(self):
        new_state: cython.int = random.randint(1, 100)
        new_node = Node(new_state, parent=self)
        self.children.append(new_node)
        return new_node

    @cython.ccall
    def update(self, result: cython.double):
        self.visits += 1
        self.value += result


@cython.ccall
def uct_search(root: Node):
    current_node = root

    while current_node.is_fully_expanded():
        current_node = current_node.best_child()

    # Simulate a result
    result: cython.double = random.random()

    # Backpropagate the result
    while current_node is not None:
        current_node.update(result)
        current_node = current_node.parent
