from random import sample

try:
    min = int(input('Введіть мінімальне значення лотерейного квитка: '))
    max = int(input('Введіть максимальне значення лотерейного квитка: '))
    quantity = int(input("Введіть кількість вгаданих чисел у квитку: "))


    # Функція, що генерує вказану кількість унікальних чисел у заданому діапазоні
    def get_numbers_ticket(min, max, quantity):
        if min >= 1 and max <= 1000:
            lottery_numbers = sorted(sample(range(min, max), quantity))
            return lottery_numbers

        else:
            return list()


    print(f'Ваші лотерейні числа {get_numbers_ticket(min, max, quantity)}')

except ValueError:
    print(f'Невірний формат лотерейних чисел.')