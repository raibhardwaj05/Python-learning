class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_have_questions(self):
        question_no = len(self.question_list)

        if self.question_number < question_no:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]

        self.question_number += 1

        attempt = input(f"Q.{self.question_number}: {current_question.ques}. (True/False)?: ").lower()

        if attempt == current_question.ans:
            print("Correct")
            self.score += 1
            print("Score: ", self.score)
        else:
            print("Incorrect")
            print("Score: ", self.score)


