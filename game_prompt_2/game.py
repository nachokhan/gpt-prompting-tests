
import json
import random
from datetime import datetime

# Function to load questions from a JSON file
def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions

# Function to update history in a JSON file
def update_history(filename, player_data):
    try:
        with open(filename, 'r') as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []
    
    history.append(player_data)
    with open(filename, 'w') as file:
        json.dump(history, file, indent=4)

# Main game function
def play_game(questions_filename, history_filename):
    # Load questions
    questions = load_questions(questions_filename)
    random.shuffle(questions)

    # Initialize game variables
    player_name = input("Enter your name: ")
    correct_answers = 0
    consecutive_incorrect_answers = 0
    total_questions_asked = 0
    total_correct_answers = 0

    # Game loop
    while correct_answers < 5 and consecutive_incorrect_answers < 2:
        question = questions[total_questions_asked % len(questions)]
        print(f"\nQuestion: {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        answer = input("Your answer (1-4): ")
        total_questions_asked += 1

        if question['options'][int(answer)-1] == question['answer']:
            correct_answers += 1
            total_correct_answers += 1
            consecutive_incorrect_answers = 0
            print("Correct!")
        else:
            consecutive_incorrect_answers += 1
            print("Incorrect!")

    # Game result
    game_result = "won" if correct_answers == 5 else "lost"
    print(f"\nYou {game_result}!")

    # Display statistics
    print(f"\nStatistics for {player_name}:")
    print(f"Total Questions Asked: {total_questions_asked}")
    print(f"Total Correct Answers: {total_correct_answers}")

    # Update history
    player_data = {
        "name": player_name,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "result": game_result,
        "statistics": {
            "total_questions_asked": total_questions_asked,
            "total_correct_answers": total_correct_answers
        }
    }
    update_history(history_filename, player_data)

# Paths to the questions and history files
questions_file = 'game_prompt_2/questions.json'
history_file = 'game_prompt_2/history.json'

# Run the game
if __name__ == "__main__":
    play_game(questions_file, history_file)
