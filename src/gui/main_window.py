import tkinter as tk
from PIL import Image, ImageTk
import gui.camera_frame as camera_frame
import gui.quiz_frame as quiz_frame
import gui.score_frame as score_frame

PROJECT_TITLE = "ForestFood"
RESOLUTION_X, RESOLUTION_Y = 720, 480
IMG_RESOLUTION_X, IMG_RESOLUTION_Y = 360, 240

class MainWindow():
    def __init__(self, root):
        self.root = root
        
        root.geometry("{0}x{1}".format(RESOLUTION_X, RESOLUTION_Y))
        root.title(PROJECT_TITLE)

        #######################################################################
        # Headbar Frame
        self.headbar_frame = tk.Frame(root, bg="grey", height=40)
        self.headbar_frame.pack(side=tk.TOP, fill=tk.X, expand=False)

        filler = tk.Frame(self.headbar_frame, width=5, height=1, bg="grey")
        filler.pack(side=tk.LEFT)

        self.menu_photo = ImageTk.PhotoImage(Image.open("./src/gui_images/mushroom.png").resize((20, 20), Image.BICUBIC))
        self.menu_icon = tk.Label(self.headbar_frame, image=self.menu_photo, bg="grey")
        self.menu_icon.pack(side=tk.LEFT)
        self.menu_icon.bind("<Button-1>", self.menu_pressed)

        self.title = tk.Label(self.headbar_frame, text=PROJECT_TITLE, bg="grey", fg="white", font="Comfortaa 16 bold")
        self.title.pack(side=tk.TOP)
        #######################################################################
        # Arrow Frames
        self.arrow_frame = tk.Frame(self.root)
        self.arrow_frame.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.back_arrow_image = ImageTk.PhotoImage(Image.open("./src/gui_images/back_arrow.png").resize((35,35), Image.BICUBIC))
        self.back_arrow_icon = tk.Label(self.arrow_frame, image=self.back_arrow_image)
        self.back_arrow_icon.pack(side=tk.LEFT)
        self.back_arrow_icon.bind("<Button-1>", self.back_arrow_pressed)

        self.forward_arrow_image = ImageTk.PhotoImage(Image.open("./src/gui_images/arrow.png").resize((35,35), Image.BICUBIC))
        self.forward_arrow_icon = tk.Label(self.arrow_frame, image=self.forward_arrow_image)
        self.forward_arrow_icon.pack(side=tk.RIGHT)
        self.forward_arrow_icon.bind("<Button-1>", self.forward_arrow_pressed)
        #######################################################################
        # Footer Frame
        self.footer = tk.Frame(self.root, height=40, bg="gray")
        self.footer.pack(side=tk.BOTTOM, fill=tk.X, expand=False)
        ########################################################################
        self.body_frame = camera_frame.CameraFrame(self.root)
        

    def menu_pressed(self, event):
        pass


    def back_arrow_pressed(self, event):
        self.quiz_frame_transition()


    def camera_frame_transition(self):
        self.body_frame.unpack()
        self.body_frame = camera_frame.CameraFrame(self.root)


    def quiz_frame_transition(self):
        self.body_frame.unpack()
        self.body_frame = quiz_frame.QuizFrame(self.root, self.score_frame_transition)


    def score_frame_transition(self, score):
        self.body_frame.unpack()
        self.body_frame = score_frame.ScoreFrame(self.root, self.quiz_frame_transition, self.camera_frame_transition)
        self.body_frame.update_score(score)


    def forward_arrow_pressed(self, event):
        self.camera_frame_transition()
