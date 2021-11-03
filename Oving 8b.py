

class QuestionGame:
    def __init__(self, question_txt, answer_alternatives, correct_answer):
        self.question_txt = question_txt
        self.answer_alternatives = list(answer_alternatives)
        self.correct_answer = int(correct_answer)

    def questions(self):
        return '\n'.join('{}: {}'.format(*k) for k in enumerate(self.answer_alternatives, 1))

    def __str__(self):
        return f"{self.question_txt}?\n" \
               f"{self.questions()}"\


    def check_answer(self, answer):
        if answer == self.correct_answer:
            print("Thats correct!\n")
        else:
            print("Sorry, thats not correct\n")


if __name__ == '__main__':
    a = ["Amsterdam", "Rotterdam", "Den Haag", "Tilburg", "Eindhoven"]

    question1 = "Whats the capitol of the Netherlands"
    answer1 = 1

    question2 = "Where was the company Phillips founded?"
    answer2 = 5

    q1 = QuestionGame(question1, a, answer1)
    print(q1)
    qq1 = int(input("Write in your answer here: "))
    q1.check_answer(qq1)

    q2 = QuestionGame(question2, a, answer2)
    print(q2)
    qq2 = qq1 = int(input("Write in your answer here: "))
    q2.check_answer(qq2)
