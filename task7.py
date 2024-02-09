import random
import matplotlib.pyplot as plt
from collections import defaultdict


# Задаємо кількість спроб
nums = 10_000_000
# Створюємо словник для накопичення результатів і заповнимо його
counts = defaultdict(int)
for _ in range(nums):
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    counts[dice_one + dice_two] += 1
# Відсортуємо і виведемо отримані резульати у таблиці так на графіку
probabilities = {key: count / nums for key, count in counts.items()}
ordered_probabilities = dict(sorted(probabilities.items()))
print(ordered_probabilities)
print("Dice | Probability")
print("-----|------------")
for dice, prob in ordered_probabilities.items():
    print(f"{dice}    | {prob:.2%}")
plt.bar(probabilities.keys(), probabilities.values())
plt.show()