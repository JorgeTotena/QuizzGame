import random

from question_model import Question
from data import question_data

question_bank = []

for i in question_data:
    text = i["text"]
    answer = i["answer"]
    new_q = Question(text =text, answer=answer)
    question_bank.append(new_q)



print(question_bank)

