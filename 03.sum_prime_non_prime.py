sum_primes_num = 0
non_primes_num_sum = 0
num_is_negative = False
num_is_prime = False
command = ""

while True:
    command = input()
    if command != "stop":
        num = int(command)
        if num > 1:
            for number in range(1, num + 1):
                if num % number == 0 and number != 1 and number != num:
                    num_is_prime = False
                    break
                else:
                    continue
            else:
                num_is_prime = True
            if num_is_prime:
                sum_primes_num += num
            else:
                non_primes_num_sum += num
        if num < 0:
            print("Number is negative.")
    else:
        break

print(f"Sum of all prime numbers is: {sum_primes_num}")
print(f"Sum of all non prime numbers is: {non_primes_num_sum}")
