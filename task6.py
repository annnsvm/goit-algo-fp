def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості у спадаючому порядку
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info["cost"] <= budget:
            selected_items.append(item_name)
            total_cost += item_info["cost"]
            total_calories += item_info["calories"]

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def dynamic_programming(items, budget):
    num_items = len(items)
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for j in range(budget + 1):
            current_item = items[list(items.keys())[i - 1]]

            if current_item["cost"] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(
                    dp_table[i - 1][j],
                    dp_table[i - 1][j - current_item["cost"]]
                    + current_item["calories"],
                )

    selected_items = []
    i, j = num_items, budget

    while i > 0 and j > 0:
        if dp_table[i][j] != dp_table[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    selected_items.reverse()
    total_cost = sum(items[item]["cost"] for item in selected_items)
    total_calories = sum(items[item]["calories"] for item in selected_items)

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dynamic_result = dynamic_programming(items, budget)

    print("Жадібний алгоритм:")
    print("Обрані страви:", greedy_result["selected_items"])
    print("Всього застрат:", greedy_result["total_cost"])
    print("Всього калорій:", greedy_result["total_calories"])
    print()
    print("Динамічное програмування:")
    print("Обрані страви:", dynamic_result["selected_items"])
    print("Всього застрат:", dynamic_result["total_cost"])
    print("Всього калорій:", dynamic_result["total_calories"])


if __name__ == "__main__":
    main()