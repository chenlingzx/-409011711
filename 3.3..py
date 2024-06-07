t_score = 0
t_student = 0
t_pass = 0
t_fail = 0

while True:
    score = float(input())
    if score == -1:
        break
    t_score += score
    t_student += 1
    if score > 59:
        t_pass += 1
    else:
        t_fail += 1

print('全班人數為:', t_student, '；', '及格人數為:', t_pass, '；', '不及格人數為:', t_fail, '全班平均為:', t_score / t_student)
