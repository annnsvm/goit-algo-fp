import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Свій ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_n = x - 1 / 2 ** layer
            pos[node.left.id] = (left_n, y - 1)
            left_n = add_edges(graph, node.left, pos, x=left_n, y=y - 1,
                               layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_n = x + 1 / 2 ** layer
            pos[node.right.id] = (right_n, y - 1)
            right_n = add_edges(graph, node.right, pos, x=right_n, y=y - 1,
                                layer=layer + 1)
    return graph


def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    # Використання значення вузла для міток
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500,
            node_color=colors)
    plt.show()


# Створення купи
root = Node(90)
root.left = Node(78)
root.left.left = Node(77)
root.left.right = Node(6)
root.right = Node(42)
root.right.left = Node(8)
root.right.right = Node(1)

# Відображення купи
draw_heap(root)