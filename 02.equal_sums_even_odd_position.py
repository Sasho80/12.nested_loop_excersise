num_first = int(input())
num_second = int(input())

odd_sum = 0
even_sum = 0
num_counter = 1

for number in range(num_first, num_second + 1):
    num_to_str = str(number)
    for digit in num_to_str:
        digit = int(digit)
        if num_counter % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        num_counter += 1
    if even_sum == odd_sum:
        print(num_to_str, end=" ")
    odd_sum = 0
    even_sum = 0
    num_counter = 0
