"""
SecuQuiz - Security Awareness CLI Quiz Game
"""
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from quiz_engine import QuizEngine

def load_questions():
    """Load questions from JSON file"""
    try:
        with open('data/questions.json', 'r') as file:
            data = json.load(file)
            return data['questions']
    except FileNotFoundError:
        print("Error: questions.json file not found!")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in questions file!")
        return []

def main():
    print("Welcome to SecuQuiz - Cybersecurity Awareness Quiz!")
    print("Loading questions")
    questions = load_questions()
    
    if not questions:
        print("No questions loaded. Exiting.")
        return
    
    print(f"Successfully loaded {len(questions)} questions!")
    
    # Start the quiz
    quiz = QuizEngine(questions)
    quiz.run_quiz()

if __name__ == "__main__": 
    main()