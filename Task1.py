from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        difference = current_date - input_date
        return difference.days
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
        return None

today = "2024-01-28"
result = get_days_from_today("2021-10-09")

if result is not None:
    print(f"Кількість днів між  {today} та 2021-10-09: {result} днів.")