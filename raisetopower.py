def raise_to_power(base, power):
    result = 1
    for number in range(power):
        result = base ** power
        return result
print(raise_to_power(3, 3))