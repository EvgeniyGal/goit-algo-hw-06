import networkx as nx


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
    G_weighted.add_weighted_edges_from(weighted_edges)
    return G_weighted


def task_3_dijkstra_algorithm():
    """Реалізує алгоритм Дейкстри для знаходження найкоротшого шляху за вагою."""
    G_weighted = create_weighted_graph()
    print("\n--- ⚖️ ЗАВДАННЯ 3: Алгоритм Дейкстри ---")

    # Використання вбудованого алгоритму Дейкстри (функція all_pairs)
    print("Результати Дейкстри: Найкоротші шляхи (за вагою) між усіма парами вершин:")

    all_paths_lengths = dict(nx.all_pairs_dijkstra_path_length(G_weighted))

    for source_node, targets in all_paths_lengths.items():
        print(f"\n--- З ДЖЕРЕЛА: {source_node} ---")
        for target_node, length in targets.items():
            if source_node != target_node:
                # Знаходимо сам шлях
                path = nx.dijkstra_path(G_weighted, source_node, target_node)
                print(f"  -> До {target_node}: Вага={length}, Шлях={path}")


if __name__ == "__main__":
    task_3_dijkstra_algorithm()
