import re


def normalize_phone(phone_number: str) -> str:
    number = re.sub(r'\D+', '', phone_number)
    if not number.startswith('38'):
        number = '38' + number
    return '+' + number
