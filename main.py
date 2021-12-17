from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Creating a question bank that contains all questions in the form of Question Objects:
question_bank = []
for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz Challenge")
print(f" Your final score is: {quiz.score}/{quiz.question_number}")