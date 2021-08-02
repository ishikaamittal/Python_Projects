from quiz_brain import QuizBrain
from question_model import Questions
from data import question_data

question_bank = []

for i in question_data:
    q = i["question"]
    ans = i["correct_answer"]
    ques = Questions(q, ans)
    question_bank.append(ques)

play = QuizBrain(question_bank)

while play.still_has_questions():
    play.next_question()

print("You have completed the quiz ")
print(f"You score {play.score}/{play.question_number}")
