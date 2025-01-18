class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    #INCREASES THE NUMBER OF THE QUESTION AND PRINTS THE CURRENT STATE
    def next_question(self,):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    # ANGELA'S solution to the still has questions methd, this functionality allows to loop within the
    # remaining questions and determine if there are still question availables for the game

    def still_has_questions(self):
        return self.question_number <= len(self.question_list)-1

#CHECKING THAT THE ANSWER FROM THE USER IS CORRECT
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    #My solution to the Still has questions challenge
    """def still_has_questions(self, q_list):
        total_questions = len(self.question_list)
        questions_available = True
        while questions_available == True:
            if self.question_number <= total_questions -1:
                self.next_question(q_list)
            else:
                questions_available = False
                print("Game has ended") """