import itertools

def count_codes(letters, repeat):

    count = 0
    for code in itertools.product(letters, repeat=repeat):
        count_j = code.count('Й')
        
        if count_j > 1:
            continue
        
        if count_j == 1:
            pos_j = code.index('Й')
            
            if pos_j == 0 or pos_j == repeat - 1:
                continue
            
            if (pos_j > 0 and code[pos_j - 1] == 'И') or \
               (pos_j < repeat - 1 and code[pos_j + 1] == 'И'):
                continue
        
        count += 1
    return count

def div_by_2(a):
    count = 0
    while a > 0:
        if a % 2 == 1:
            count += 1
        a //= 2
    return count

def div_finder():
    left, right = 174457, 174505
    result = []

    for n in range(left, right + 1):
        divisors = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d != n // d:
                    divisors.append(n // d)
            d += 1
        if len(divisors) == 2:
            divisors.sort()
            result.append((n, divisors[0], divisors[1]))

    result.sort(key=lambda x: x[0])

    for _, d1, d2 in result:
        print(d1, d2)

letters = ['Т', 'И', 'М', 'О', 'Ф', 'Е', 'Й']
result_1 = count_codes(letters, 5)
print(f"Количество различных кодов: {result_1}")

result_2 = div_by_2(4**2020 + 2**2017 - 15)
print(result_2)

div_finder()
