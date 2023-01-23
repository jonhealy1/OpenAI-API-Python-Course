from teacher import Teacher

class Exam:
    def __init__(self, student_view, answers):
        self.student_view = student_view
        self.answers = answers
    
    def take(self):
        answers = {}
        for question, question_view in self.student_view.items():
            print(question_view)
            answer = input("Enter your answer: ")
            answers[question] = answer
        return answers

    def grade(self, answers):
        correct_answers = 0
        for question, answer in answers.items():
            if answer.upper() == self.answers[question].upper()[16]:
                correct_answers+=1
        return 100 * correct_answers / len(answers)



if __name__ == "__main__":
    teacher = Teacher()
    student_view, answers = teacher.create_full_test()

    exam = Exam(student_view, answers)
    student_answers = exam.take()
    print(student_answers)
    grade = exam.grade(student_answers)
    print(grade)
