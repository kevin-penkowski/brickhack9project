import tkinter as tk
import gui.main_window as main_window
from PIL import Image, ImageTk

class HomepageFrame():
    def __init__(self, parent, quiz_transition_func):
        self.parent = parent

        self.frame = tk.Frame(self.parent)
        self.frame.pack(expand=True)

        self.title = tk.Label(self.frame, text=main_window.PROJECT_TITLE, font=("Arial", 56, "bold"))
        self.title.pack(side=tk.TOP)

        self.diagram = ImageTk.PhotoImage(Image.open("./src/gui_images/mushroom_diagram.jpg").resize((120,200), Image.BICUBIC))
        self.diagram_label = tk.Label(self.frame, image=self.diagram)
        self.diagram_label.pack()

        self.button = tk.Button(self.frame, text="Take our quiz!", command=quiz_transition_func)
        self.button.pack(side=tk.BOTTOM)





    def unpack(self):
        self.frame.pack_forget()
