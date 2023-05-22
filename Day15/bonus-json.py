import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

try:
    for question in data:
        print(question["question_text"])
        for index, item in enumerate(question["alternatives"]):
            print(index + 1, question["alternatives"][index])
        user_answer = int(input("Number of correct answer: "))
        question["user_choice"] = user_answer
except ValueError:
    exit("Enter a number please")


correct = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        result = "Correct answer"
        correct += 1
    else:
        result = "Wrong answer"

    message = f"{index + 1} - correct answer to {question['question_text']} was: {question['correct_answer']} - " \
              f"{question['alternatives'][question['correct_answer'] - 1]} " \
              f"\nYour answer: {question['user_choice']} - {question['alternatives'][question['user_choice'] - 1]}\n" \
              f"which was {result}"
    print(message)

print(f"Correct {correct}/{len(data)}")
