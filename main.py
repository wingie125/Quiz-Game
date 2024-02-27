from typing import Union, Dict, Any

from data import question_data
from Question_paper  import question_paper
from quiz_brain import QuizBrain


question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=question_paper(question_text,question_answer)
    question_bank.append(new_question)


quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.new_question()

print("You have completed the quiz")
print(f"Your final score : {quiz.score}/{quiz.question_number}")
