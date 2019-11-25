# This Python script aims to exclude non-participant from image dataset

# import modules
import os
import json
import cv2
import numpy as npshutil
import shutil
from IBAtS_global import ROOT_DIR, NONPARTICIPANT_TAG, HEXDEC, bgr, rgb


def is_nonparticipant_exist(faces):
    '''Detect whether any non-participant is exist within the list of faces'''
    for face in faces:
        if face['color'] == NONPARTICIPANT_TAG:
            return True
    return False


def remove_nonparticipant(fpath, fname, faces):
    '''Remove non-participant from image dataset by blocking facial region
    with red rectangular area'''
    img = cv2.imread(os.path.join(fpath, fname))

    for face in faces:
        if face['color'] == NONPARTICIPANT_TAG:
            tickness = -1
            (x, y, w, h, color) = (face['x'], face['y'],
                                   face['width'], face['height'], face['color'])
            cv2.rectangle(img, (x, y), (x + w, y + h),
                          bgr(rgb(color[1:])), tickness)
    cv2.imwrite(filename=os.path.join(fpath, fname), img=img)


def exclude_nonparticipant(fpath, fname):
    '''Exclude non-participant from image dataset'''

    json_fname = '{fname}.gold.json'.format(fname=fname[:-4])
    with open(os.path.join(fpath, json_fname), 'r+') as json_file:
        gold_json = json.load(json_file)

    faces = gold_json
    if is_nonparticipant_exist(faces):
        remove_nonparticipant(fpath, fname, faces)


def main():
    '''main function'''
    classrooms = os.listdir(ROOT_DIR)
    for classroom in classrooms:
        dates = os.listdir(os.path.join(ROOT_DIR, classroom))
        for date in dates:
            fpath = os.path.join(ROOT_DIR, classroom, date)
            fnames = os.listdir(fpath)
            for fname in fnames:
                if fname.startswith('[resize]') and fname.endswith('.jpg'):
                    exclude_nonparticipant(fpath=fpath, fname=fname)


if __name__ == "__main__":
    main()
