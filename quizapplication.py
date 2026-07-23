# Simple Quiz Application

print("===== Welcome to the Quiz =====")

score = 0

# Questions and Answers
questions = [
    ["What is the capital of India?", "Delhi"],
    ["How many days are there in a week?", "7"],
    ["Which planet is known as the Red Planet?", "Mars"],
    ["What is 5 + 8?", "13"],
    ["What is the national animal of India?", "Tiger"]
]

# Loop through questions
for i in range(len(questions)):
    print("\nQuestion", i + 1)
    print(questions[i][0])

    answer = input("Your Answer: ")

    # Condition to check answer
    if answer.lower() == questions[i][1].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", questions[i][1])

# Display Result
print("\n===== Quiz Result =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

# Grade using conditions
if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")
