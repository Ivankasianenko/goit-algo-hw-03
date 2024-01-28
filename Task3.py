import re
def normalize_phones(phone_number):
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)
    if cleaned_number.startswith('+'):
        normalized_number = cleaned_number
    else:
        normalized_number = '+38' + cleaned_number
    return normalized_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",]

normalized_numbers = [normalize_phones(num) for num in raw_numbers]
print(normalized_numbers)