from datetime import datetime

 # Функція для перетворення рядка дати у форматі "РРРР-ММ-ДД" у об'єкт datetime
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

# Функція, що розраховує кількість днів між заданою датою та поточною
def get_days_from_today(date):
    difference_date = string_to_date(target_day) - current_date
    return difference_date.days

try:
    target_day = input("Задайте необхідну дату у форматі РРРР-ММ-ДД: ")
    current_date = datetime.now().today().date()
    print(f'Поточна дата: {current_date}')
    print(f'Різниця між заданою датою та поточною: {get_days_from_today(target_day)} днів')

except ValueError:
    print(f'Невірний формат необхідної дати.')

