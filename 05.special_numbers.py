num = int(input())
start_num = 1111
end_num = 9999
num_to_str = 0
counter = 0
special_num = 0

for n in range(start_num, end_num):
    num_to_str = str(n)
    counter = 0
    for digit in num_to_str:
        digit = int(digit)
        if digit == 0:
            break
        elif num % digit == 0:
            counter += 1
            continue
        else:
            break
    if counter == len(num_to_str):
        special_num = num_to_str
        print(special_num, end=" ")
    else:
        continue
