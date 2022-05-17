class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {item.text} (True/False)?: ")
        self.check_answer(guess, item.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, guess, correct_answer):
        if guess.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("")

