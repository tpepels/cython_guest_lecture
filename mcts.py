import math
import random


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0

    def is_fully_expanded(self):
        return len(self.children) > 0

    def best_child(self, exploration_weight=1.414):
        best_score = -float("inf")
        best_child = None

        for child in self.children:
            exploitation = child.value / child.visits
            exploration = exploration_weight * math.sqrt(
                math.log(self.visits) / child.visits
            )
            score = exploitation + exploration
            if score > best_score:
                best_score = score
                best_child = child

        return best_child

    def expand(self):
        # In a real MCTS, this would generate new game states
        # For simplicity, we simulate adding a random child
        new_state = random.randint(1, 100)
        new_node = Node(new_state, parent=self)
        self.children.append(new_node)
        return new_node

    def update(self, result):
        self.visits += 1
        self.value += result


def uct_search(root):
    current_node = root

    while current_node.is_fully_expanded():
        current_node = current_node.best_child()

    # Simulate a result (in a real scenario, this would be game outcome)
    result = random.random()

    # Backpropagate the result up the tree
    while current_node is not None:
        current_node.update(result)
        current_node = current_node.parent


if __name__ == "__main__":
    root = Node(0)

    for _ in range(1000):  # Simulate 1000 UCT iterations
        uct_search(root)

    print(f"Root visits: {root.visits}, Root value: {root.value}")
