import random

def get_numbers_ticket(min_num, max_num, quantity):
    if min_num < 1 or max_num > 1000 or min_num >= max_num or quantity < 1 or quantity > (max_num - min_num + 1):
        return []
    numbers_set = set()
    while len(numbers_set) < quantity:
        random_number = random.randint(min_num, max_num)
        numbers_set.add(random_number)
    return sorted(list(numbers_set))

min_value = 1
max_value = 1000
quantity = 15
result = get_numbers_ticket(min_value, max_value, quantity)

if result:
    print(f"Ваш лотерейний квиток: {result}")
else:
    print("Помилка в параметрах. Повернуто пустий список.")