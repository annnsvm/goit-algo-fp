import heapq


def dijkstra(graph, start_point):
    # Створимо словник для зберігання ваги ребер
    # І задамо спочатку, що вони всі нескінченні
    distances = {vertex: float('infinity') for vertex in graph}
    # Відстань до початкової вершини дорівнює 0
    distances[start_point] = 0
    # Создамо чергу приорітетів для зберігання вершин і їх відстаней у купі
    priority_queue = [(0, start_point)]
    while priority_queue:
        # Достанему з купи верину з найменьшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)
        # Якщо ця відстань до вершини більше, ніж збережене, то ігноруємо її
        if current_distance > distances[current_vertex]:
            continue
        # Розглянемо всі сусідні вершини поточної
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Якщо знайшли більш короткий шлях до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances


if __name__ == "__main__":
    # Задамо граф
    graph = {
        'A': {'B': 4, 'C': 7},
        'B': {'A': 4, 'D': 2, 'E': 8},
        'C': {'A': 7, 'D': 2, 'E': 5},
        'D': {'B': 2, 'C': 2, 'E': 1, 'F': 4},
        'E': {'C': 5, 'D': 1, 'F': 11},
        'F': {'B': 8, 'D': 4, 'E': 11}
    }
    # Викличемо функцію для розрахунку відстаней від вершини 'А'
    result = dijkstra(graph, 'A')
    # Виведемо отримані результати
    print('Найкоротший шлях до кожної вершини:')
    for vertex, distance in result.items():
        print(f"До вершини {vertex}: {distance}")