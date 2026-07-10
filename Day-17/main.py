# Project quiz 2
from  question_model import Question
from data import question_data
from quiz_brain import  QuizBrain
# question1=Question()
question_bank=[]

for questions in question_data:
   
    question_text =questions['question']
    question_answer=questions['correct_answer']
    new_question =Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
# quiz.check_answer(question_bank,question_answer)
# quiz.score
print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

    


# print(bank_question[0].text,"\n",bank_question[0].answer)

# print(bank_question[1].text,"\n",bank_question[1].answer)

# print(bank_question[2].text,"\n",bank_question[2].answer)
