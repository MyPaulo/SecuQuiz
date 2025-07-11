"Core quiz logic"

from utils import print_header, print_success, print_error, print_info, print_question_header, print_warning
from colorama import Fore, Style
from collections import defaultdict


class QuizEngine:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.total_questions = len(questions)

        #Track catgeory performance
        self.category_stats = defaultdict(lambda: {'correct': 0, 'total': 0})
        # Initialize category counts
        for question in questions:
            self.category_stats[question['category']]['total'] += 1

    def display_question(self, question):
        "Display a single questions with options"
        print_question_header(self.current_question + 1, self.total_questions)
        print_info(f"Category: {question['category'].title()}")
        print(f"{Fore.WHITE}{Style.BRIGHT}Q: {question['question']}{Style.RESET_ALL}")
        print()
        for option in question['options']:
            print(f" {option}")
        print()
    
    def get_user_answer(self):
        "get user input for processing answer"
        while True:
            answer = input(f"{Fore.YELLOW}Your answer (A, B, C or D): {Style.RESET_ALL}").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            else:
                print_error("Please enter A, B, C, or D only.")

    def check_answer(self, user_answer, correct_answer):
        "check if user answer is right"
        return user_answer == correct_answer
    
    def display_result(self, is_correct, explanation, category):
        "display if answer is right and show explanation"
        if is_correct:
            print_success("Correct!")
            self.score +=1
            self.category_stats[category]['correct'] += 1
        else:
            print_error("Incorrect.")
        print(f"{Fore.CYAN}Explanation: {explanation}{Style.RESET_ALL}")
        print("-" * 50)

    def run_quiz(self):
        "Run complete Quiz"
        print_header("CYBERSECURITY AWARENESS QUIZ")
        print("Answer each question by typing A, B, C, or D.")
        print("=" * 60)

        for question in self.questions:
            self.display_question(question)
            user_answer = self.get_user_answer()
            is_correct = self.check_answer(user_answer, question['correct_answer'])
            self.display_result(is_correct, question['explanation'], question['category'])
            
            self.current_question += 1

            # wait between questions (except for the last one)
            if self.current_question < self.total_questions:
                input(f"{Fore.YELLOW}Press Enter to continue to next question...{Style.RESET_ALL}")

        self.display_final_score()

    def display_category_breakdown(self):
        """Display performance breakdown by category"""
        print_header("CATEGORY BREAKDOWN")
        
        for category, stats in self.category_stats.items():
            correct = stats['correct']
            total = stats['total']
            percentage = (correct / total) * 100 if total > 0 else 0
            
            # Color code based on performance
            if percentage >= 80:
                color = Fore.GREEN
            elif percentage >= 60:
                color = Fore.YELLOW
            else:
                color = Fore.RED
            
            print(f"{color}{Style.BRIGHT}{category.title()}: {correct}/{total} ({percentage:.1f}%){Style.RESET_ALL}")
            

    def display_final_score(self):
        "Display final score and performance"
        print_header("QUIZ COMPLETED!")
    
        percentage = (self.score / self.total_questions) * 100
        print(f"{Fore.WHITE}{Style.BRIGHT}Your Score: {self.score}/{self.total_questions}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{Style.BRIGHT}Percentage: {percentage:.1f}%{Style.RESET_ALL}")
        
        if percentage >= 80:
            print_success("Excellent! You have good cybersecurity awareness.")
        elif percentage >= 60:
            print_info("Good job! Keep learning about cybersecurity.")
        else:
            print_warning("Consider reviewing cybersecurity basics.")
    
        # Show category breakdown (only once)
        self.display_category_breakdown()

        # Show recommendations
        self.show_recommendations()


    def show_recommendations(self):
        """Show learning recommendations based on weak areas"""
        print_header("RECOMMENDATIONS")
        
        weak_categories = []
        for category, stats in self.category_stats.items():
            correct = stats['correct']
            total = stats['total']
            percentage = (correct / total) * 100 if total > 0 else 0
            
            if percentage < 60:
                weak_categories.append(category)
        
        if weak_categories:
            print("Consider focusing on these areas:")
            for category in weak_categories:
                print(f"{Fore.YELLOW}• {category.title()}{Style.RESET_ALL}")
        else:
            print_success("Great job! You're strong in all categories.")

