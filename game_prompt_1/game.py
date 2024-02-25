
import random
import json

def load_questions():
    with open("game_prompt_1/questions.json", "r") as file:
        return json.load(file)

def play_game(questions):
    correct_answers = 0
    wrong_streak = 0

    while True:
        category = random.choice(list(questions.keys()))
        question = random.choice(questions[category])

        print(f"\nCategory: {category}")
        print(f"Q: {question['question']}")
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")
        answer = input("Your answer (number): ")

        if question['options'][int(answer) - 1] == question['answer']:
            print("Correct!")
            correct_answers += 1
            wrong_streak = 0
        else:
            print("Wrong!")
            wrong_streak += 1

        if correct_answers == 3:
            print("You win!")
            break
        elif wrong_streak == 2:
            print("You lose!")
            break

if __name__ == "__main__":
    questions = load_questions()
    organized_questions = {}
    for question in questions:
        category = question['category']
        if category not in organized_questions:
            organized_questions[category] = []
        organized_questions[category].append(question)
    play_game(organized_questions)
