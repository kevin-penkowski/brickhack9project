import numpy as np
import csv
#odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s
#gill color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y
#stalk texture (above and below ring): fibrous=f,scaly=y,silky=k,smooth=s

with open("mushroom_data.csv", "r") as data_og:
    csvreader = data_og.readlines()
    #this might have to change if the decision tree fails
    data_aug = np.empty((0, 30))
    for line in range(1, len(csvreader)):
        row = csvreader[line].replace("\n", "").split(",")
        odor = row[0]
        gill_color = row[1]
        stalk_above = row[2]
        stalk_below = row[3]
        result = row[4]

        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])


        #(a, l, c, y, f, m, n, p, s)
        stitched_array = []
        odor_array = []
        gill_color_array = []
        stalk_above_array = []
        stalk_below_array = []
        decision = []

        if odor == 'a':
            odor_array = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif odor == 'l':
            odor_array = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif odor == 'c':
            odor_array = [0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif odor == 'y':
            odor_array = [0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif odor == 'f':
            odor_array = [0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif odor == 'm':
            odor_array = [0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif odor == 'n':
            odor_array = [0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif odor == 'p':
            odor_array = [0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif odor == 's':
            odor_array = [0, 0, 0, 0, 0, 0, 0, 0, 1]
        else:
            print("something has gone terribly wrong (odor)")
        
    #k, n, b, h, g, r, o, p, u, e, w, y
        if gill_color == 'k':
            gill_color_array = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif gill_color == 'n':
            gill_color_array = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif gill_color == 'b':
            gill_color_array = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif gill_color == 'h':
            gill_color_array = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif gill_color == 'g':
            gill_color_array = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] 
        elif gill_color == 'r':
            gill_color_array = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif gill_color == 'o':
            gill_color_array = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif gill_color == 'p':
            gill_color_array = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif gill_color == 'u':
            gill_color_array = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif gill_color == 'e':
            gill_color_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif gill_color == 'w':
            gill_color_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif gill_color == 'y':
            gill_color_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        else:
            print("something has gone terribly wrong (gill_color)")

        if stalk_above == 'f':
            stalk_above_array = [1, 0, 0, 0]
        elif stalk_above == 'y':
            stalk_above_array = [0, 1, 0, 0]
        elif stalk_above == 'k':
            stalk_above_array = [0, 0, 1, 0]
        elif stalk_above == 's':
            stalk_above_array = [0, 0, 0, 1]
        else:
            print("something has gone horribly wrong (stalk_above)")
        
        if stalk_below == 'f':
            stalk_below_array = [1, 0, 0, 0]
        elif stalk_below == 'y':
            stalk_below_array = [0, 1, 0, 0]
        elif stalk_below == 'k':
            stalk_below_array = [0, 0, 1, 0]
        elif stalk_below == 's':
            stalk_below_array = [0, 0, 0, 1]
        else:
            print("something has gone horribly wrong (stalk_below)")

        
        if result == 'e':
            decision = [1]
        elif result == 'p':
            decision = [0]
        else:
            print("something has gone horribly wrong (result)")
        
        stitched_array = np.append(stitched_array, odor_array)
        stitched_array = np.append(stitched_array, gill_color_array)
        stitched_array = np.append(stitched_array, stalk_above_array)
        stitched_array = np.append(stitched_array, stalk_below_array)
        stitched_array = np.append(stitched_array, decision)
        #print(stitched_array)

        data_aug = np.vstack([data_aug, stitched_array])
        np.save('mushroom_data_aug.npy', data_aug)

    data_aug = np.load("mushroom_data_aug.npy")

    lines = data_aug

    n = [0, 1]
    features = [i[0:-1] for i in lines if i != ""]
    features = np.array(features, dtype = "uint8")

    decision = [i[-1] for i in lines if i != ""]
    decision = np.array(decision)

    i = np.argsort(np.random.random(features.shape[0]))
    features = features[i]
    decision = decision[i]

    np.save("mushroom_features.npy", features)
    np.save("mushroom_labels.npy", decision)

