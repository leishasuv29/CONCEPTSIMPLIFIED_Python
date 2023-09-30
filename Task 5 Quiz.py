"""Develop a quiz game that asks users multiple-choice or fill-in-the-blank questions on a specific topic. The game should keep track
of scores, provide feedback on correct/incorrect answers, and offer a variety of questions to make it challenging and engaging."""

import random

# Define a list of quiz questions as dictionaries
quiz_questions = [
    {
        "question": "Who is the captain of Royal Challengers Bangalore?",
        "options": ["Faf Du Plesis", "Virat Kohli", "Glenn Maxwell", "AB Devilliers"],
        "correct_answer": "1"
    },
    {
        "question": "Which of these teams has only appeared in the IPL final once?",
        "options": ["Kolkata Knight Riders", "Royal Challengers Bangalore", "Sunrisers Hyderabad", "Punjab Kings"],
        "correct_answer": "4"
    },
    {
        "question": "Where was the first IPL match played?",
        "options": ["Bangalore", "Mumbai", "Kolkata", "Chennai"],
        "correct_answer": "1"
    }
]

def ask_question(question_dict):
    print(question_dict["question"])
    for i, option in enumerate(question_dict["options"], 1):
        print(f"{i}. {option}")
    user_answer = input("Enter the number of your answer: ")
    return user_answer

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def display_result(score, total_questions):
    print(f"You got {score} out of {total_questions} questions correct!")

def quiz_game():
    print("Welcome to the IPL Quiz Game!")
    print("You will be asked multiple-choice questions. Enter the number of your answer.")

    play_again = "yes"
    while play_again.lower() == "yes":
        random.shuffle(quiz_questions)
        score = 0
        total_questions = len(quiz_questions)

        for question in quiz_questions:
            user_answer = ask_question(question)
            if check_answer(user_answer, question["correct_answer"]):
                print("Correct!\n")
                score += 1
            else:
                print(f"Sorry, the correct answer is: {question['correct_answer']}\n")

        display_result(score, total_questions)
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    quiz_game()