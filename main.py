from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    text = i["question"]
    answer = i["correct_answer"]
    new_q = Question(text =text, answer=answer)
    question_bank.append(new_q)

# print(question_bank[0].text)

quiz = QuizBrain(question_bank)
#quiz.next_question(question_bank)
#quiz.still_has_questions(question_bank) from my solution to the challenge

while quiz.still_has_questions():
    quiz.next_question()

print("you've completed the quiz")
print(f"your score was {quiz.score}/{quiz.question_number}")
