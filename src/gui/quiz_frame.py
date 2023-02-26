import tkinter as tk
from dataclasses import dataclass
from PIL import Image, ImageTk
import json

QUIZ_QUESTION_FILEPATH = "./src/quiz_questions.json"

class QuizFrame():
    def __init__(self, parent, transition_to_score_func):
        self.parent = parent
        self.transition_to_score_func = transition_to_score_func
    
        self.quiz_questions = decode_questions(QUIZ_QUESTION_FILEPATH)
        self.correct_answers_count = 0
        self.current_question_index = -1
        self.current_question = self.quiz_questions[self.current_question_index]
        #######################################################################
        self.question_frame = tk.Frame(parent)
        self.question_frame.pack()

        self.question_label = tk.Label(self.question_frame)
        self.question_label.pack()

        self.question_img_label = tk.Label(self.question_frame)
        self.question_img_label.pack()
        #######################################################################
        self.answers_frame = tk.Frame(parent)
        self.answers_frame.pack()

        self.answer_buttons = list()
        #######################################################################
        self.next_question()


    def next_question(self):
        self.answers_frame.pack_forget()
        self.answers_frame = tk.Frame(self.parent)
        self.answers_frame.pack()

        if self.current_question_index == len(self.quiz_questions)-1:
            self.score_answers()
            return
        
        self.current_question_index += 1
        self.current_question = self.quiz_questions[self.current_question_index]

        self.question_label.config(text=self.current_question.question)
        
        if (self.current_question.question_img_path != ""):
            self.current_question_image = ImageTk.PhotoImage(Image.open(self.current_question.question_img_path).resize((200,200), Image.BICUBIC))
        else:
            self.current_question_image = ImageTk.PhotoImage(Image.open("./src/gui_images/quiz_images/blank.png").resize((10,10), Image.BICUBIC))

        self.question_img_label.config(image=self.current_question_image)
        self.answer_buttons = list()
        for i in range(len(self.current_question.answers)):
            answer = self.current_question.answers[i]
            answer_command = self.correct_answer if i == self.current_question.correct_answer else self.incorrect_answer
            answer_button = tk.Button(self.answers_frame, text=answer, command=answer_command)
            answer_button.grid(row=i, column=0)
            self.answer_buttons.append(answer_button)


    def correct_answer(self):
        self.correct_answers_count += 1
        self.next_question()


    def incorrect_answer(self):
        self.next_question()


    def score_answers(self):
        score = self.correct_answers_count / len(self.quiz_questions)
        self.transition_to_score_func(score)


    def unpack(self):
        self.question_frame.pack_forget()
        self.answers_frame.pack_forget()


@dataclass
class QuizQuestion():
    question: str
    answers: list
    correct_answer: int
    question_img_path: str


def decode_questions(filepath):
    data = ""
    f = open(filepath)
    data = json.load(f)
    f.close()
    quiz_questions = list()
    for question in data["questions"]:
        question_str = question["question"]
        answers = question["answers"]
        correct_answer = question["correct_answer"]
        question_img_path = question["question_img_path"]
        quiz_questions.append(QuizQuestion(question=question_str, answers=answers, correct_answer=correct_answer, question_img_path=question_img_path))
    return quiz_questions
