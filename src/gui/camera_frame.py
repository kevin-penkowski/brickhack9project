import tkinter as tk
from PIL import Image, ImageTk
from gui.classification import Classification
import cv2
import datetime
import gui.main_window as main_window

class CameraFrame():
    def __init__(self, root):
        ###########################################################################################
        # Parent Frame
        self.parent = root
        ###########################################################################################
        # Camera Frame
        self.body = tk.Frame(self.parent)
        self.body.pack(expand=True)

        filler_x, filler_y = (main_window.RESOLUTION_X-main_window.IMG_RESOLUTION_X)/2, main_window.IMG_RESOLUTION_Y
        self.filler_frame = tk.Frame(self.body, width=filler_x, height=filler_y)

        self.frame = tk.Frame(self.body)
        self.frame.pack()

        self.camera_label = tk.Label(self.frame, text="Opening Camera...", width=main_window.IMG_RESOLUTION_X, height=main_window.IMG_RESOLUTION_Y)
        self.camera_label.pack()

        self.camera_icon_photo = ImageTk.PhotoImage(Image.open("./src/gui_images/camera.png").resize((50,50), Image.NEAREST))
        self.camera_icon = tk.Label(self.frame, image=self.camera_icon_photo)
        self.camera_icon.pack()
        self.camera_icon.bind("<Button-1>", self.camera_icon_pressed)
        ###########################################################################################
        # Footer Frame
        self.footer = tk.Frame(self.parent, height=40)
        self.footer.pack(side=tk.BOTTOM, fill=tk.X, expand=False)

        self.classification_label = tk.Label(self.footer, font="Comfortaa 16 bold", fg="white")
        self.classification_label.pack()
        self.classification = None
        self.update_classification_label(Classification.UNCLASSIFIED)
        ###########################################################################################
        self.capture = cv2.VideoCapture(0)
        self.camera_label.after(20, self.show_frame_in_window)


    def show_frame_in_window(self):
        # Get the latest frame and convert into Image
        try: 
            resized = cv2.resize(self.capture.read()[1], (main_window.IMG_RESOLUTION_X, main_window.IMG_RESOLUTION_Y))
            flipped = cv2.flip(resized, 1)
            cv2image= cv2.cvtColor(flipped,cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)

            # Convert image to PhotoImage
            self.camera_img = ImageTk.PhotoImage(image = img)
            self.camera_label.configure(image=self.camera_img)
            #loop
            self.camera_label.after(25, self.show_frame_in_window)
        except:
            pass
        


    def update_classification_label(self, new_classification):
        if new_classification == self.classification:
            return
        else:
            self.classification_label.config(text=new_classification.value["text"], bg=new_classification.value["color"])
            self.footer.config(bg=new_classification.value["color"])
            self.classification = new_classification


    def camera_icon_pressed(self, event):
        now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filepath = "./saved_images/foodForest{0}.png".format(now)
        cv2.imwrite(filepath, self.capture.read()[1])


    def unpack(self):
        self.body.pack_forget()
        self.footer.pack_forget()
        self.capture.release()
