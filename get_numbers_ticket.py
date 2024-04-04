import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    min_max_range = range(min, max + 1)
    if min < 0 or max > 1000 or quantity not in min_max_range:
        return []
    else:
        return sorted(random.sample(min_max_range, quantity))

print(get_numbers_ticket(1,1000,10))
print(get_numbers_ticket(1,5,5))
print(get_numbers_ticket(1,1000,1001))
print(get_numbers_ticket(1,1000,0))
