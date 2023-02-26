import tkinter as tk

class ScoreFrame():
    def __init__(self, parent, quiz_transition_func, camera_transition_func):
        self.parent = parent

        self.frame = tk.Frame(parent)
        self.frame.pack()

        self.score_label = tk.Label(self.frame)
        self.score_label.pack()

        self.transition_buttons_frame = tk.Frame(parent)
        self.transition_buttons_frame.pack()

        self.quiz_transition_btn = tk.Button(self.transition_buttons_frame, text="Play Again!", command=quiz_transition_func)
        self.quiz_transition_btn.grid(row=0, column=0)

        self.camera_transition_btn = tk.Button(self.transition_buttons_frame, text="To The Camera!", command=camera_transition_func)
        self.camera_transition_btn.grid(row=0, column=1)

    def update_score(self, score):
        score_text = "You scored a {0} percent on the quiz! Woo-Hoo!".format(str(round(score*100, 2)))
        self.score_label.config(text=score_text)

    def unpack(self):
        self.frame.pack_forget()
        self.transition_buttons_frame.pack_forget()
