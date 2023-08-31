import random

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": 2  # Index of correct answer (starting from 0)
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": 0  # Index of correct answer (starting from 0)
    },
    {
        "question": "What is the largest mammal?",
        "choices": ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": 1  # Index of correct answer (starting from 0)
    }
    # Add more questions here
]

def display_question(question_data):
    print(question_data["question"])
    for idx, choice in enumerate(question_data["choices"]):
        print(f"{idx + 1}. {choice}")

def get_user_choice():
    return int(input("Enter your choice: ")) - 1

def evaluate_answer(user_choice, correct_answer):
    return user_choice == correct_answer

def play_quiz():
    score = 0
    total_questions = len(quiz_questions)
    
    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")
    
    for idx, question_data in enumerate(quiz_questions):
        print(f"\nQuestion {idx + 1}/{total_questions}")
        display_question(question_data)
        user_choice = get_user_choice()
        
        if evaluate_answer(user_choice, question_data["correct_answer"]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer was: {question_data['choices'][question_data['correct_answer']]}")
    
    print("\nQuiz completed!")
    print(f"Your score: {score}/{total_questions}")
    
    if score == total_questions:
        print("Congratulations! You got all the questions right!")
    elif score >= total_questions / 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing to improve.")
    
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"

if __name__ == "__main__":
    play = True
    while play:
        play = play_quiz()
