"""
Задача: Анкета актеров

Даны входные данные (вы можете скопировать этот текст в исходный код)

actor1_name    = "Leonardo DiCaprio"
actor1_country = "США"
actor1_birth   = 1974

actor2_name    = "Brad Pitt"
actor2_country = "США"
actor2_birth   = 1963

actor3_name    = "Асель Садвакасова"
actor3_country = "Казахстан"
actor3_birth   = 1985

actor4_name    = "Санжар Мади"
actor4_country = "Казахстан"
actor4_birth   = 1986

years = [2026, 2000, 1990]

Для каждого актёра посчитать возраст в 2026, 2000, 1990
Посчитать возраст в месяцах (на 2026)
Найти сумму и среднее возрастов в 2026
Найти разницу между самым старшим и самым младшим
Собрать итоговый отчёт одной строкой

Пример результата, который необходимо получить:

=== АНКЕТА АКТЁРОВ ===

Leonardo DiCaprio (США)
  Возраст в 2026: 52
  Возраст в 2000: 26
  Возраст в 1990: 16
  Возраст в месяцах (на 2026): 624

Brad Pitt (США)
  Возраст в 2026: 63
  Возраст в 2000: 37
  Возраст в 1990: 27
  Возраст в месяцах (на 2026): 756

Asel Sadvakasova (Казахстан)
  Возраст в 2026: 41
  Возраст в 2000: 15
  Возраст в 1990: 5
  Возраст в месяцах (на 2026): 492

Санжар Мади (Казахстан)
  Возраст в 2026: 40
  Возраст в 2000: 14
  Возраст в 1990: 4
  Возраст в месяцах (на 2026): 480

=== ИТОГИ ===
Суммарный возраст в 2026: 196
Средний возраст в 2026: 49.0
Разница между самым старшим и самым младшим (2026): 23
Самый старший: Brad Pitt (63)
Самый младший: Санжар Мади (40)

=== ОТЧЁТ ===
В 2026 году 4 актёра имеют средний возраст 49.0 лет. Самый старший — Brad Pitt (63), самый младший — Санжар Мади (40).

"""


actor1_name = "Leonardo DiCaprio"
actor1_country = "США"
actor1_birth = 1974

actor2_name = "Brad Pitt"
actor2_country = "США"
actor2_birth = 1963

actor3_name = "Асель Садвакасова"
actor3_country = "Казахстан"
actor3_birth = 1985

actor4_name = "Санжар Мади"
actor4_country = "Казахстан"
actor4_birth = 1986

years = [2026, 2000, 1990]

# Возраст каждого актёра
age1 = 2026 - actor1_birth
age2 = 2026 - actor2_birth
age3 = 2026 - actor3_birth
age4 = 2026 - actor4_birth

# Список возрастов
ages = [age1, age2, age3, age4]

# Сумма и средний возраст
total = sum(ages)
average = total / len(ages)

# Самый старший и младший
oldest_age = max(ages)
youngest_age = min(ages)

difference = oldest_age - youngest_age

names = [actor1_name, actor2_name, actor3_name, actor4_name]

oldest_name = names[ages.index(oldest_age)]
youngest_name = names[ages.index(youngest_age)]

# Анкета
print("=== АНКЕТА АКТЁРОВ ===")

print(f"\n{actor1_name} ({actor1_country})")
for year in years:
    print(f"  Возраст в {year}: {year - actor1_birth}")
print(f"  Возраст в месяцах (на 2026): {age1 * 12}")

print(f"\n{actor2_name} ({actor2_country})")
for year in years:
    print(f"  Возраст в {year}: {year - actor2_birth}")
print(f"  Возраст в месяцах (на 2026): {age2 * 12}")

print(f"\n{actor3_name} ({actor3_country})")
for year in years:
    print(f"  Возраст в {year}: {year - actor3_birth}")
print(f"  Возраст в месяцах (на 2026): {age3 * 12}")

print(f"\n{actor4_name} ({actor4_country})")
for year in years:
    print(f"  Возраст в {year}: {year - actor4_birth}")
print(f"  Возраст в месяцах (на 2026): {age4 * 12}")

# Итоги
print("\n=== ИТОГИ ===")
print(f"Суммарный возраст в 2026: {total}")
print(f"Средний возраст в 2026: {average}")
print(f"Разница между самым старшим и самым младшим (2026): {difference}")
print(f"Самый старший: {oldest_name} ({oldest_age})")
print(f"Самый младший: {youngest_name} ({youngest_age})")

# Отчёт одной строкой
print("\n=== ОТЧЁТ ===")
print(f"В 2026 году {len(ages)} актёра имеют средний возраст {average} лет. Самый старший — {oldest_name} ({oldest_age}), самый младший — {youngest_name} ({youngest_age}).")
