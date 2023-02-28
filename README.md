
ForestFood
Collaberators: Kevin Penkowski, Tianna Seitz, Daniel Bossett, Cameron Dalton
BrickHacks 9 Submission

What is ForestFood?
ForestFood is an ML-powered classifier to determine the edibleness of mushrooms found in the wild. This project aims to help foraging beginners and enthusiasts make informed decisions about what is safe to consume.
The hobby of foraging has seen spike in popularity since the start of the COVID-19 pandemic. Encouraged to spend time in nature, many people started looking towards consumables that are growing naturally in their communities to provide a new and exciting addition to their nutrition. Foraging has also been a part of many sustainability initiatives! But how do you know what is safe to consume? Professional foragers always warn about dangerous lookalikes, especially amongst the fungi kingdom. This is a great tool for hobbies to get more comfortable with the mushrooms they find. This tool is not to be used without prior knowledge and reading on safe mushroom consumption. Though we encourage beginners to use this tool, no one should go into foraging totally blind

Dependencies:

openCV
Numpy
Sklearn
TKinter

    
How to use:
Currently, ForestFood is in the prototyping phase. This means the full list of features that can classify a poison mushroom has not been implemented. For proof of concept, we have chosen 4. Our classifier is based on a decision tree and is implemented into the GUI. The computer vision is still a work in progress, but there is sample code of image manipulation techniques we started working on.

Before our software can be used, users must complete a quiz to show that they have done some amount of research and will not become a liability.

Our next steps are to fully implement the image segmentation and feature classification network. Supported by image processing and our server for mushroom features beyond the survey, we would like to implement more features found in our training and testing dataset to more confidently tell consumers whether their mushroom findings are likely to be poisonous.

Here is the intended use:

Open the application and arrive at the homepage. The homepage has preliminary information that will help you complete the quiz
Complete the quiz to gain access to our software's features
Find a mushroom and take a picture of it in the software. You will get a preliminary classification of the mushroom.
Fill in the form for features that cannot be detected via an image (example: mushroom odor)
Gain a classification as to whether or not the mushroom is safe to consume

Other information:

We do not own the following datasets:
The dataset we used in mushroom_data_raw.csv was found at: https://www.kaggle.com/datasets/uciml/mushroom-classification 
The mushroom image dataset was found at: https://www.kaggle.com/datasets/maysee/mushrooms-classification-common-genuss-images?resource=download
We used an image of the mushroom gills in the quiz from this site: https://www.jungledragon.com/image/68132/the_adnate_gills_of_the_golden_trumpet_mushroom.html