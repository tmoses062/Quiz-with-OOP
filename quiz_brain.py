class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < 12

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        print("\n")

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {question_answer.title()}")
        print(f"Your current score is: {self.score}/{self.question_number}")

    def final_score(self):
        if self.question_number == 12:
            print("You've completed the quiz")
            print(f"Your final score is: {self.score}/{self.question_number}")
