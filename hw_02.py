from random import sample

# Функція, що генерує вказану кількість унікальних чисел у заданому діапазоні
def get_numbers_ticket(min , max, quantity):
    if min >= 1 and max <= 1000:
        return sorted(sample(range(min, max), quantity))
    else:
        return list()

try:
    min = int(input('Введіть мінімальне значення лотерейного квитка: '))
    max = int(input('Введіть максимальне значення лотерейного квитка: '))
    quantity = int(input("Введіть кількість вгаданих чисел у квитку: "))

    lottery_numbers = get_numbers_ticket(min, max, quantity)

    print(f'Ваші лотерейні числа {lottery_numbers}')

except ValueError:
    print(f'Невірний формат лотерейного квитка ')
