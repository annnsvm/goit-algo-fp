import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    # To heap list
    def to_heap_list(self):
        heap_list = []

        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                heap_list.append(node.val)
                inorder_traversal(node.right)

        inorder_traversal(self)
        return heap_list

    def __lt__(self, other):
        return self.val < other.val


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


# Add adges
def add_heap_edges(graph, heap, pos, index=0, x=0, y=0, layer=1):
    if index < len(heap):
        node = heap[index]
        graph.add_node(node.id, color=node.color, label=node.val)
        if 2 * index + 1 < len(heap):
            graph.add_edge(node.id, heap[2 * index + 1].id)
            l = x - 1 / 2**layer
            pos[heap[2 * index + 1].id] = (l, y - 1)
            add_heap_edges(
                graph, heap, pos, 2 * index + 1, x=l, y=y - 1, layer=layer + 1
            )
        if 2 * index + 2 < len(heap):
            graph.add_edge(node.id, heap[2 * index + 2].id)
            r = x + 1 / 2**layer
            pos[heap[2 * index + 2].id] = (r, y - 1)
            add_heap_edges(
                graph, heap, pos, 2 * index + 2, x=r, y=y - 1, layer=layer + 1
            )


# visualize_heap
def draw_heap(heap):
    heap_graph = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}
    add_heap_edges(heap_graph, heap, pos)

    colors = [node[1]["color"] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap_graph,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


def main():
    heap = [Node(0), Node(4), Node(5), Node(10), Node(1), Node(3)]
    heapq.heapify(heap)

    # Відображення бінарної купи
    draw_heap(heap)


if __name__ == "__main__":
    main()