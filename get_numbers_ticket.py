import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    result = []
    
    if min > 0 and max <= 1000 and min <= quantity <= max:
        while len(result) < quantity:
            number = random.randint(min, max)
        
            if number in result:
                continue
            else:
                result.append(number)

        return sorted(result)
    else:
        return result

print(get_numbers_ticket(1,1000,50))
print(get_numbers_ticket(1,5,5))
print(get_numbers_ticket(1,1000,5550))
