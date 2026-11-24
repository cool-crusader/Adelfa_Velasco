# Sean Gabriel Velasco
# 8-Adelfa

score = []

for i in range(5):
    scores = int(input(f"Input quiz {i+1} grades: "))
    score.append(scores)

sum = sum(score)
average_grade = sum / len(score)
highest_score = max(score)
lowest_score = min(score)
ascending_grade = sorted(score)
descending_grade = sorted(score, reverse=True)


print("===== QUIZ SCORE REPORT =====")
print("Number of Quizzes: 5")
print(f"Total score: {sum} ")
print(f"Average score: {average_grade:.2f} ")
print(f"Highest score: {highest_score} ")
print(f"Lowest score: {lowest_score} ")
print(f"Ascending grade: {ascending_grade} ")
print(f"Descending grade: {descending_grade} ")
print(f"Original score: {scores.append(scores)} ")
