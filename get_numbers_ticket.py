import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    result = []
    while len(result) < quantity:
        number = random.randint(min, max)
        
        if number in result:
            continue
        else:
            result.append(number)

    return sorted(result)

print(get_numbers_ticket(1,1000,50))
print(get_numbers_ticket(1,5,5))
