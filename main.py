# Завдання 1. «Швидкий пошук»
cities = ["Київ", "Одеса", "Львів", "Харків", "Житомир"]
city_set = set(cities)

for city in ["Одеса", "Полтава"]:
    if city in city_set:
        print(f"Місто {city} присутнє у списку.")
    else:
        print(f"Місто {city} відсутнє у списку.")

print("\n" + "-"*40 + "\n")

# Завдання 2. «Пошук за словником»
students = {"Іван": 80, "Марія": 95, "Олег": 78, "Анна": 85}

name = input("Введіть ім'я студента: ")
try:
    print(f"Оцінка студента {name}: {students[name]}")
except KeyError:
    print(f"Студента з іменем {name} не знайдено у словнику.")

print("\n" + "-"*40 + "\n")

# Завдання 3. «Оптимізація повторів»
import random
numbers = [random.randint(1, 1000) for _ in range(10000)]

frequency = {}
for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

most_common = max(frequency.items(), key=lambda x: x[1])
print(f"Число, яке повторюється найчастіше: {most_common[0]}")
print(f"Кількість повторень: {most_common[1]}")
