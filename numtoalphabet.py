def number_to_alphabet(n):
    if not (1 <= n <= 702):
        return "Input out of range (1-702)"
    
    result = ""
    while n > 0:
        n -= 1
        result = chr(n % 26 + ord('A')) + result
        n //= 26
    
    return result

n = int(input("Enter a number (1-702): "))
print(number_to_alphabet(n))
