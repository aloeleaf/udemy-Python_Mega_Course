import json

with open('questions.json') as file_local:
    content = file_local.read()

data = json.loads(content)

for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives']):
        print(f"{index + 1}-{alternative}")
    user_choice = int(input("Enter the number of the correct answer: "))
    question["user_choice"] = user_choice

score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Incorrect Answer"

    message = f"{result} {index + 1} - Your answer: {question['user_choice']}, "\
        f"Correct answer: {question['correct_answer']}"
    print(message)

print(score, "/", len(data))
