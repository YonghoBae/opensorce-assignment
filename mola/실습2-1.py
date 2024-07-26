print('학생 그룹 점수의 합계와 평균을 구합니다.')

n_students = int(input("학생 수를 입력하세요: "))

scores = []
for i in range(n_students):
    score = int(input(f"{i+1}번 학생의 점수를 입력하세요: "))
    scores.append(score)

def calculate_scores(scores):
    total = 0
    min_score = scores[0]
    max_score = scores[0]
    for score in scores:
        total += score
        if score < min_score:
            min_score = score
        if score > max_score:
            max_score = score
    average = total / len(scores)
    return total, average, min_score, max_score

total_score, average_score, min_score, max_score = calculate_scores(scores)
print(f"합계: {total_score}, 평균: {average_score}, 최저점: {min_score}, 최고점: {max_score}")
