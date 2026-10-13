# Sean Gabriel Velasco
# 8-Adelfa
# Student Performance Evaluator



name = ""
score1 = 0
score2 = 0
score3 = 0
average = 0

def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")

def get_student_info():
    name = input("Name: ")
    score1 = float(input("Assessment1: "))
    score2 = float(input("Assessment2: "))
    score3 = float(input("Assessment3: "))

    return name, score1, score2, score3
get_student_info()

def evaluate_performance():
    average = (score1 + score2 + score3) / 3
    if average >= 90:
        return"Outstanding"
    elif average >= 85:
        return "Very Satisfactory"
    elif average >= 80:
        return "Satisfactory"
    elif average >= 75:
        return "Fairly Satisfactory"
    else:
        return "Needs Improvement"

def display_report():
    print("STUDENT PERFORMANCE EVALUATOR")
    print(f"Assessment Scores: {score1}, {score2}, {score3}")
    print(f"Average Score: {average:.2f}")
    print("Performance Level: ")

display_header()
get_student_info()
evaluate_performance()
display_report()