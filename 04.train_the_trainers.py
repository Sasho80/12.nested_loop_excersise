num_people_jury = int(input())
command = ""
n_num_rating = 0
counter_rating = 0
average_score = 0.0
sum_score = 0.0
all_sum_score = 0.0

while command != "Finish":
    name_presentation = input()
    if name_presentation == "Finish":
        break
    else:
        for n in range(1, num_people_jury + 1):
            n_num_rating = float(input())
            sum_score += n_num_rating
            counter_rating += 1
    average_score = 0
    all_sum_score += sum_score
    average_score += sum_score/num_people_jury
    sum_score = 0
    print(f"{name_presentation} - {average_score:.2f}.")

print(f"Student's final assessment is {all_sum_score/counter_rating:.2f}.")
