# brickhack9project

<head>
    <header>
        <h1>ForestFood</h1>
        <h4>Collaberators: Kevin Penkowski, Tianna Seitz, Daniel Bozsett, Cameron Dalton</h4>
        <h4>BrickHacks 9 Submission</h4>
    </header>
</head>
<body>
    <h3>What is ForestFood?</h3>
    <p>ForestFood is an ML powered classifier to determine the edibleness of mushrooms found in the wild. This project aims to help foraging beginingers and enthusiasts make informed decisions about what is safe to consume.</p>

    <h3>Dependencies:</h3>
        <ul>
            <li>openCV</li>
            <li>Numpy</li>
            <li>Sklearn</li>
            <li>TKinter</li>
        </ul>
    
    <h3>How to use:</h3>
    <p>Currently, ForestFood is in the prototyping phase. This means that the full list of features that can classify a poison mushroom have not been implemented. For proof of concept, we have chosen 4. Our classifier is based off a decision tree and is implemented into the GUI. The computer vision is still a work in progress, but there is sample code of image manipulation techniques we started working on.</p>
    <p>Before our software can be used, users must complete a quiz to show that they have done some amount of research and will not become a liability.</p>
    <p>Here is the intended use:
        <ol>
            <li>Open the application and arrive at homepage. The homepage has preliminary information that will help you complete the quiz</li>
            <li>Complete the quiz to gain access to our software's features</li>
            <li>Find a mushroom and take a picture of it in the software. You will get a preliminary classification of the mushroom.</li>
            <li>Fill in the form for features that cannot be detected via image (example: mushroom odor)</li>
            <li>Gain a classification as to whether or not the mushroom is safe to consume</li>
        </ol>
    </p>
    <h3>Other information </h3>
    <p>We do not own the following datsets: </p>
    <p>The dataset we used in mushroom_data_raw.csv was found at: https://www.kaggle.com/datasets/uciml/mushroom-classification </p>
    <p>The mushroom image dataset was found at: https://www.kaggle.com/datasets/maysee/mushrooms-classification-common-genuss-images?resource=download</p>
    <p>We used an image of the mushroom gills in the quiz from this site: https://www.jungledragon.com/image/68132/the_adnate_gills_of_the_golden_trumpet_mushroom.html</p>
</body>