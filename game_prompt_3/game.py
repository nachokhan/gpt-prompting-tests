
import json
import random
import datetime

def load_questions():
    with open('game_prompt_3/questions.json') as file:
        return json.load(file)

def update_history(player_name, correct, incorrect):
    with open('game_prompt_3/history.json', 'r+') as file:
        history = json.load(file)
        history['games'].append({
            'player': player_name,
            'correct': correct,
            'incorrect': incorrect,
            'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        file.seek(0)
        json.dump(history, file, indent=4)

def ask_question(question):
    print(question['question'])
    for i, choice in enumerate(question['choices']):
        print(f'{i + 1}. {choice}')
    try:
        answer = int(input('Enter your answer (1-4): '))
        return question['choices'][answer - 1] == question['answer']
    except (ValueError, IndexError):
        print('Invalid input. Please enter a number between 1 and 4.')
        return False

def main():
    questions = load_questions()
    random.shuffle(questions)
    correct_answers = 0
    wrong_streak = 0
    questions_asked = 0

    player_name = input('Enter your name: ')
    print(f'Welcome, {player_name}! Let\'s start the game.')

    while correct_answers < 5 and wrong_streak < 2 and questions_asked < len(questions):
        if ask_question(questions[questions_asked]):
            correct_answers += 1
            wrong_streak = 0
            print('Correct!')
        else:
            wrong_streak += 1
            print('Incorrect!')
        questions_asked += 1

    if correct_answers == 5:
        print('Congratulations, you won!')
    else:
        print('Game over!')
    
    print(f'You answered {correct_answers} questions correctly out of {questions_asked} questions asked.')
    update_history(player_name, correct_answers, questions_asked - correct_answers)

if __name__ == '__main__':
    main()
