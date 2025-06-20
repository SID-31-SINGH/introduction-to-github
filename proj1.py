import random

def create_quiz_questions():
    """
    Defines the quiz questions, options, and correct answers.
    Returns a list of dictionaries, where each dictionary represents a question.
    """
    questions = [
        {
            "question": "What is the capital of France?(Use certain options)",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the 'Red Planet'?(Use certain options)",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?(Use certain options)",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Who painted the Mona Lisa?(Use certain options)",
            "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?(Use certain options)",
            "options": ["A. O2", "B. H2O", "C. CO2", "D. NaCl"],
            "answer": "B"
        }
    ]
    return questions

def run_quiz(questions):
    """
    Runs the quiz game, presents questions, tracks score, and collects answers.
    
    Args:
        questions (list): A list of question dictionaries.

    Returns:
        tuple: A tuple containing the user's score and the total number of questions.
    """
    score = 0
    total_questions = len(questions)
    
    # Shuffle questions to provide a different experience each time
    random.shuffle(questions)

    print("--- Welcome to the Quiz Game! ---")
    print("Answer the following multiple-choice questions. Enter A, B, C, or D.\n")

    for i, q_data in enumerate(questions):
        print(f"Question {i + 1}/{total_questions}: {q_data['question']}")
        for option in q_data['options']:
            print(f"  {option}")
        
        user_answer = input("Your answer: ").strip().upper()

        if user_answer == q_data['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q_data['answer']}.\n")
    
    return score, total_questions

def display_results(score, total_questions):
    """
    Displays the final quiz results and provides feedback.
    
    Args:
        score (int): The user's final score.
        total_questions (int): The total number of questions in the quiz.
    """
    print("--- Quiz Finished! ---")
    print(f"You scored {score} out of {total_questions} questions.")

    percentage = (score / total_questions) * 100

    if percentage == 100:
        print("Congratulations! You got a perfect score!")
    elif percentage >= 70:
        print("Great job! You have a good understanding of the topics.")
    elif percentage >= 50:
        print("Good effort! Keep practicing to improve.")
    else:
        print("You might need to review some topics. Don't give up!")

    print("\nThanks for playing!")

def main():
    """
    Main function to orchestrate the quiz game.
    """
    quiz_questions = create_quiz_questions()
    final_score, num_questions = run_quiz(quiz_questions)
    display_results(final_score, num_questions)

if __name__ == "__main__":
    main()
