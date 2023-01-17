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
        return correct_answers



if __name__ == "__main__":
    teacher = Teacher("Python")
    student_view, answers = teacher.create_full_test(4, 4)
    print(student_view)
    print(answers)

    exam = Exam(student_view, answers)
    student_answers = exam.take()
    print(student_answers)
    grade = exam.grade(student_answers)
    print(grade)
