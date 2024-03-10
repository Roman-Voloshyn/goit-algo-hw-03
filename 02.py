import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    tickets = set()
    while len(tickets) < quantity:
        tickets.add(random.randint(min, max))
    return sorted(tickets)
