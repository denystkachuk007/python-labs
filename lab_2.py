# Завдання 1. Розрахунок та інтерпретація ІМТ

print("\n--- Розрахунок ІМТ ---")

# 1. Введення даних
height = float(input("Введіть зріст у метрах: "))
weight = float(input("Введіть масу в кг: "))

# 2. Обчислення ІМТ
BMI = weight / (height ** 2)

# 3. Визначення результату
print("\n--- Результати обчислень ---")
print(f"ІМТ: {BMI:.2f}")

if BMI < 18.5:
    print("Висновок: underweight (мала маса)")
elif BMI <= 24.9:
    print("Висновок: normal weight (нормальна маса)")
else:
    print("Висновок: overweight (надмірна маса)")

# Завдання 2. Перевірка промокоду на знижку

print("\n--- Перевірка промокоду ---")

# 1. Введення даних
bill_amount = float(input("Введіть суму чека (грн): "))
promo_code = input("Введіть промокод: ")

# 2. Визначення знижки
if promo_code == "SALE10":
    discount = 10
elif promo_code == "SALE20":
    discount = 20
else:
    discount = 0

# 3. Обчислення знижки та фінальної суми
discount_amount = bill_amount * discount / 100
final_amount = bill_amount - discount_amount

# 4. Виведення результатів
print("\n--- Результати обчислень ---")
print(f"Знижка: {discount}%")
print(f"Сума знижки: {discount_amount:.2f} грн")
print(f"Фінальна сума: {final_amount:.2f} грн")

