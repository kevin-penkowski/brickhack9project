from functools import partial
import tkinter as tk
from ml.data_editor import convert_feature_to_symbol, breakdown_into_features
import ml.decision_tree as decision_tree
from gui.classification import Classification
import numpy as np

class FormFrame():
    def __init__(self, parent):
        self.parent = parent
        self.clf = decision_tree.create_clf()
        x_train, y_train = decision_tree.get_training_set()
        decision_tree.train(x_train, y_train, self.clf)

        f = open("./src/features.csv", "r")
        self.features_dict = dict()
        for line in f.readlines():
            line = line.replace("\n", "")
            tokens = line.split(",")
            feature_name = tokens[0]
            feature_categories = tokens[1:]
            self.features_dict[feature_name] = feature_categories
        

        self.frame = tk.Frame(parent)
        self.frame.pack()

        self.features_selected = dict()
        for feature_name in self.features_dict.keys():
            self.features_selected[feature_name] = self.features_dict[feature_name][0]

        count_features = -1
        for feature_name in self.features_dict.keys():
            count_features += 1
            feature_label = tk.Label(self.frame, text=feature_name)
            feature_label.grid(row=count_features, column=0)
            count_feature_categories = -1
            buttons = list()
            for j in range(len(self.features_dict[feature_name])):
                count_feature_categories += 1
                feature_category = self.features_dict[feature_name][j]
                button = tk.Button(self.frame, text=feature_category)
                cmd = partial(self.update_selected_value, feature_name, feature_category, button, buttons)
                button.config(command=cmd)
                button.grid(row=count_features, column=count_feature_categories+1)
                buttons.append(button)

        self.submit_button = tk.Button(self.frame, text="SUBMIT FOR CLASSIFICATION", command=self.submit)
        self.submit_button.grid(row=count_features+1, column=0)
        ###########################################################################################
        # Footer Frame
        self.footer = tk.Frame(self.parent, height=40)
        self.footer.pack(side=tk.BOTTOM, fill=tk.X, expand=False)

        self.classification_label = tk.Label(self.footer, font="Comfortaa 16 bold", fg="white")
        self.classification_label.pack()
        self.classification = None
        self.update_classification_label(Classification.UNCLASSIFIED)
        ###########################################################################################


    def update_selected_value(self, feature_name, selected_value, button, buttons):
        self.features_selected[feature_name] = selected_value
        for b in buttons:
            b.config(bg='#F0F0F0')
            b["state"] = "normal"
        button.config(bg="red")
        button["state"] = "disabled"
        


    def update_classification_label(self, new_classification):
        if new_classification == self.classification:
            return
        else:
            self.classification_label.config(text=new_classification.value["text"], bg=new_classification.value["color"])
            self.footer.config(bg=new_classification.value["color"])
            self.classification = new_classification


    def submit(self):
        symbols = dict()
        for feature_name in self.features_selected.keys():
            selected_feature = self.features_selected[feature_name]
            symbols[feature_name] = convert_feature_to_symbol(selected_feature)
        breakdown = breakdown_into_features(
            odor=symbols["odor"], 
            gill_color=symbols["color"], 
            stalk_above=symbols["stalk surface above ring"], 
            stalk_below=symbols["stalk surface below ring"]
        )
        result = decision_tree.predict( np.reshape(breakdown, (1, -1)), self.clf)[0]
        print("ODOR:{0}\nCOLOR:{1}\nABOVE:{2}\nBELOW:{3}\nRESULT:{4}".format(
            self.features_selected["odor"], 
            self.features_selected["color"], 
            self.features_selected["stalk surface above ring"],
            self.features_selected["stalk surface below ring"],
            result
        ))
        if result == 0.0:
            self.update_classification_label(Classification.DANGEROUS)
        elif result == 1.0:
            self.update_classification_label(Classification.SAFE)
        
        
    def unpack(self):
        self.frame.pack_forget()
        self.footer.pack_forget()
