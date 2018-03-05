# This Python script aims to automate face detection prior to manual tagging
# procedure to form a gold standard dataset

# import modules
import cv2
import os
import json
from IBAtS_global import ROOT_DIR, CASCADE_DIR, FACE_CLSF


def detect_faces(filepath, classifier, scaleFactor=1.1, minNeighbors=5):
    '''Detect faces in an image and save the detection as json file'''

    # load image file
    img = cv2.imread(filepath)

    # convert image to grayscale
    gray_img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = classifier.detectMultiScale(image=gray_img,
                                        scaleFactor=scaleFactor,
                                        minNeighbors=minNeighbors)

    # record detected face areas into a list of dictionary
    faces_to_json = []
    for (x, y, w, h) in faces:
        rect = {'color': '#00ff00', 'x': int(x), 'y': int(y),
                'width': int(w), 'height': int(h)}
        faces_to_json.append(rect)

    # save detected face areas as json file
    with open(filepath[:-4] + '.json', 'w') as outfile:
        json.dump(obj=faces_to_json, fp=outfile, indent=4)


def main():
    '''main function'''
    face_classifier = cv2.CascadeClassifier(os.path.join(CASCADE_DIR,
                                                         FACE_CLSF))
    classrooms = os.listdir(ROOT_DIR)
    for classroom in classrooms:
        dates = os.listdir(os.path.join(ROOT_DIR, classroom))
        for date in dates:
            fnames = os.listdir(os.path.join(ROOT_DIR, classroom, date))
            for fname in fnames:
                if not fname.endswith('.jpg') or not fname.startswith('[resize]'):
                    # skip non jpg files or non resized jpeg files
                    continue
                filepath = os.path.join(ROOT_DIR, classroom, date, fname)
                detect_faces(filepath=filepath, classifier=face_classifier)


if __name__ == "__main__":
    main()
