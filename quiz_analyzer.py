# Sean Gabriel Velasco
# 8-Adelfa

score = []

for i in range(5):
    quiz_score = int(input(f"Enter Quiz {i+1} score: "))
    score.append(quiz_score)

total_score = sum(score)
num_quizzes = len(score)
average_grade = total_score / num_quizzes
highest_score = max(score)
lowest_score = min(score)
ascending_grade = sorted(score)
descending_grade = sorted(score, reverse=True)

print("QUIZ SCORE REPORT")
print(f"Quiz Scores: {score}")
print(f"Number of Quizzes: {num_quizzes}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_grade:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Ascending: {ascending_grade}")
print(f"Descending: {descending_grade}")
print(f"Original Scores: {score}")
