import logging

from test_creator import TestGenerator


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

dummy_test = '\n\nQ1. What type of language is Python?\nA. Object-Oriented \nB. Functional \nC. Interpreted \nD. Compiled\n\nCorrect Answer: C. Interpreted\n\nQ2. What does a variable in Python refer to?\nA. A constant value \nB. A function \nC. An object \nD. A string\n\nCorrect Answer: C. An object\n\nQ3. What is the correct syntax for creating a comment in Python?\nA. # Comment \nB. /* Comment */ \nC. // Comment \nD. -- Comment\n\nCorrect Answer: A. # Comment"'


class Teacher:
    def __init__(self, topic):
        self.topic = topic


    def create_full_test(self, num_possible_answers, num_questions):
        self.test_creator = TestGenerator(self.topic, num_possible_answers, num_questions)
        test = self.test_creator.run()
        #test = dummy_test
        logging.info(test)
        student_view = self.create_student_view(test, num_questions)
        answers = self.extract_answers(test, num_questions)
        return student_view, answers

    def create_student_view(self, test, num_questions):
        student_view = {1 : ""}
        question_number = 1
        for line in test.split("\n"):
            if not line.startswith("Correct Answer:"):
                student_view[question_number] += line+"\n"
            else:
                
                if question_number < num_questions:
                    question_number+=1
                    student_view[question_number] = ""
        return student_view

    def extract_answers(self, test, num_questions):
        answers = {1 : ""}
        question_number = 1
        for line in test.split("\n"):
            if line.startswith("Correct Answer:"):
                answers[question_number] += line+"\n"

                if question_number < num_questions:
                    question_number+=1
                    answers[question_number] = ""
        return answers

        

if __name__ == "__main__":
    teacher = Teacher("Python")
    student_view, answers = teacher.create_full_test(4, 2)
    print(student_view)
    print(answers)
