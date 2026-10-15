
data = [
    ("Пн", 5, 12),
    ("Вт", 3, 10),
    ("Ср", -2, 8),
    ("Чт", 0, 6),
    ("Пт", 7, 14),
    ("Сб", 10, 18),
    ("Вс", 8, 15),
]

temperatures = []
cold_days = []

warm_day = ""
cold_day = ""

highest = data[0][2]
lowest = data[0][1]

for day, min_t, max_t in data:
    average = (min_t + max_t) / 2
    temperatures.append(average)

    print(f"{day}: мин {min_t}, макс {max_t}, среднее {average}")

    if max_t > highest:
        highest = max_t
        warm_day = day

    if min_t < lowest:
        lowest = min_t
        cold_day = day

    if min_t < 0:
        cold_days.append(day)

week_average = sum(temperatures) / len(temperatures)

print(f"\nСредняя температура за неделю: {week_average:.2f}")
print(f"Самый тёплый день: {warm_day}, {highest}")
print(f"Самый холодный день: {cold_day}, {lowest}")
print(f"Дни с температурой ниже нуля: {cold_days}")
