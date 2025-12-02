import networkx as nx
import heapq


def create_weighted_graph():
    """Створює зважений граф для алгоритму Дейкстри."""
    G_weighted = nx.Graph()

    # Додаємо ребра з вагами (відстань/час)
    weighted_edges = [
        ("Центр", "Вокзал", 5),
        ("Центр", "Парк", 8),
        ("Центр", "Ринкова Площа", 4),
        ("Вокзал", "Житловий Масив", 12),
        ("Парк", "Бібліотека", 3),
        ("Ринкова Площа", "Університет", 7),
        ("Університет", "Бібліотека", 2),
        ("Бібліотека", "Житловий Масив", 6),
        ("Ринкова Площа", "Житловий Масив", 15),
    ]
    # Використовуємо 'weight' як ім'я атрибута ваги
    G_weighted.add_weighted_edges_from(weighted_edges)
    return G_weighted


# --- Власна Реалізація Алгоритму Дейкстри ---
def custom_dijkstra(graph, start_node):
    """
    Реалізує алгоритм Дейкстри для знаходження найкоротших шляхів від start_node.
    Використовує heapq (чергу з пріоритетом).
    """
    # 1. Ініціалізація
    # Відстані до всіх вершин (початково нескінченність)
    distances = {node: float("inf") for node in graph.nodes}
    distances[start_node] = 0

    # Словник для відновлення шляхів (prev_node)
    previous_nodes = {node: None for node in graph.nodes}

    # Черга з пріоритетом: (вага, вершина)
    priority_queue = [(0, start_node)]

    # 2. Обробка черги
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо ми вже знайшли коротший шлях до цієї вершини, ігноруємо
        if current_distance > distances[current_node]:
            continue

        # 3. Обхід сусідів
        for neighbor, data in graph[current_node].items():
            # Вага ребра
            weight = data["weight"]
            distance = current_distance + weight

            # Релаксація: Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes


def reconstruct_path(previous_nodes, start_node, end_node):
    """Відновлює шлях від кінцевої до початкової вершини."""
    path = []
    current = end_node
    while current is not None:
        path.append(current)
        if current == start_node:
            break
        current = previous_nodes[current]

    # Якщо шлях знайдено, повертаємо його у правильному порядку
    if path and path[-1] == start_node:
        return path[::-1]
    return None


def task_3_dijkstra_algorithm():
    """Реалізує алгоритм Дейкстри для знаходження найкоротшого шляху за вагою."""
    G_weighted = create_weighted_graph()
    print("\n--- ⚖️ ЗАВДАННЯ 3: Власна Реалізація Алгоритму Дейкстри ---")

    start_node = "Центр"
    end_node = "Житловий Масив"

    # Виконання власного алгоритму
    distances, previous_nodes = custom_dijkstra(G_weighted, start_node)

    print(f"Найкоротші шляхи (за вагою) від джерела: {start_node}")

    for target_node in sorted(G_weighted.nodes):
        if target_node == start_node:
            continue

        final_distance = distances[target_node]
        path = reconstruct_path(previous_nodes, start_node, target_node)

        if final_distance == float("inf"):
            print(f"  -> До {target_node}: Шлях не знайдено.")
        else:
            print(f"  -> До {target_node}: Вага={final_distance}, Шлях={path}")

    # Перевірка цільового шляху
    print(f"\nПеревірка результату для {start_node} -> {end_node}:")
    target_path = reconstruct_path(previous_nodes, start_node, end_node)
    target_weight = distances[end_node]
    print(f"  - Найкоротший шлях: {target_path}")
    print(f"  - Мінімальна сумарна вага: {target_weight}")


if __name__ == "__main__":
    task_3_dijkstra_algorithm()
