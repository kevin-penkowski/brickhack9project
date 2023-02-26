from functools import partial
import tkinter as tk

class FormFrame():
    def __init__(self, parent):
        self.parent = parent

        f = open("./src/features.csv", "r")
        features_dict = dict()
        for line in f.readlines():
            line = line.replace("\n", "")
            tokens = line.split(",")
            feature_name = tokens[0]
            feature_categories = tokens[1:]
            features_dict[feature_name] = feature_categories
        

        self.frame = tk.Frame(parent)
        self.frame.pack()

        self.features_selected = dict()
        for feature_name in features_dict.keys():
            self.features_selected[feature_name] = features_dict[feature_name][0]

        count_features = -1
        for feature_name in features_dict.keys():
            count_features += 1
            feature_label = tk.Label(self.frame, text=feature_name)
            feature_label.grid(row=count_features, column=0)
            count_feature_categories = -1
            for j in range(len(features_dict[feature_name])):
                count_feature_categories += 1
                feature_category = features_dict[feature_name][j]
                cmd = partial(self.update_selected_value, feature_name, feature_category)
                button = tk.Button(self.frame, text=feature_category, command=cmd)
                button.grid(row=count_features, column=count_feature_categories+1)

        self.submit_button = tk.Button(self.frame, text="SUBMIT FOR CLASSIFICATION", command=self.submit)
        self.submit_button.grid(row=count_features+1, column=0)


    def update_selected_value(self, feature_name, selected_value):
        self.features_selected[feature_name] = selected_value


    def submit(self):
        pass

        
    def unpack(self):
        self.frame.pack_forget()
