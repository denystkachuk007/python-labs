def max_digit_info(number):
    digits = str(number)

    max_digit = max(digits)
    count = digits.count(max_digit)

    return int(max_digit), count


max_sum = 0
max_sum_number = 0

for number in range(1, 11):
    max_digit, count = max_digit_info(number)

    digit_sum = sum(int(digit) for digit in str(number))

    print(f"Число: {number}")
    print(f"Найбільша цифра: {max_digit}")
    print(f"Кількість входжень: {count}")
    print(f"Сума цифр: {digit_sum}")
    print()

    if digit_sum > max_sum:
        max_sum = digit_sum
        max_sum_number = number


print("Число з найбільшою сумою цифр:", max_sum_number)
print("Найбільша сума цифр:", max_sum)

# Завдання 2
# Lambda-функція для отримання останньої цифри числа

last_digit = lambda number: number % 10

numbers = [123, 4567, 890, 25]

for number in numbers:
    print(f"Число: {number}, остання цифра: {last_digit(number)}")