candidate_prime_number = 57

for number in range(2, candidate_prime_number):
    if candidate_prime_number % number == 0:
        print(candidate_prime_number, "は素数ではありません")
        break
