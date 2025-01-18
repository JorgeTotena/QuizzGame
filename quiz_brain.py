class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self, q_list):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        input(f"Q.{self.question_number}: {current_question.text} (True/False) ")

    def still_has_questions(self, q_list):
        total_questions = len(self.question_list)
        questions_available = True
        while questions_available == True:
            if self.question_number <= total_questions -1:
                self.next_question(q_list)
            else:
                questions_available = False
                print("Game has ended")



