subjects = ["Anh", "Em"]
verbs = ["Chơi", "Yêu"]
objects = ["Bóng đá", "Xếp hình"]

for subject in subjects:
    for verb in verbs:
        for object in objects:
            sentence = "{} {} {}".format(subject, verb, object)
            print(sentence)