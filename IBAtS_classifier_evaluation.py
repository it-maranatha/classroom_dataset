# This Python script aims to evaluate detection results derived from four
# pre-trained classifiers toward gold standard dataset

# import modules
import os
import json
import cv2
import numpy as np
from IBAtS_global import ROOT_DIR, CLASSIFIERS, NONPARTICIPANT_TAG, load_json


def group_json_fnames(filepath):
    '''Groupping json files based on classifiers used for face detection'''
    fnames = os.listdir(filepath)
    gold_fnames = []
    alt_fnames = []
    al2_fnames = []
    tre_fnames = []
    def_fnames = []

    for fname in fnames:
        if not fname.endswith('.json') or not fname.startswith('[resize]'):
            continue
        elif fname.endswith('.gold.json'):
            gold_fnames.append(fname)
        elif fname.endswith('.alt.json'):
            alt_fnames.append(fname)
        elif fname.endswith('.al2.json'):
            al2_fnames.append(fname)
        elif fname.endswith('.tre.json'):
            tre_fnames.append(fname)
        elif fname.endswith('.def.json'):
            def_fnames.append(fname)

    gold_fnames.sort()
    alt_fnames.sort()
    al2_fnames.sort()
    tre_fnames.sort()
    def_fnames.sort()

    return {'gold': gold_fnames, 'alt': alt_fnames,
            'al2': al2_fnames, 'tre': tre_fnames,
            'def': def_fnames}


def get_rect_list(json_faces):
    '''Extract list of rectangles (x,y,w,h) from json face detection file'''
    rect_list = []
    for tag in json_faces:
        if tag['color'] == NONPARTICIPANT_TAG:
            # skip non participant
            continue
        rect_list.append([tag['x'], tag['y'], tag['width'], tag['height']])
    return rect_list


def rect_list_to_detection_list(rect_list):
    '''Convert list of rectangles into list of detections format'''
    detection_list = []
    for rect in rect_list:
        detection_list.append({'x': int(rect[0]), 'y': int(rect[1]),
                               'width': int(rect[2]), 'height': int(rect[3])})
    return detection_list


def evaluate_detection(gold, clsf_detection):
    '''Evaluate face detection produced from a classifier toward a gold standard'''
    rect_list = gold + clsf_detection
    true_pos_rects, weights = cv2.groupRectangles(rectList=rect_list,
                                                  groupThreshold=1, eps=0.2)
    true_pos = len(true_pos_rects)
    false_pos = len(clsf_detection) - true_pos
    false_neg = len(gold) - true_pos
    true_pos_detecs = rect_list_to_detection_list(true_pos_rects)

    return true_pos, false_pos, false_neg, true_pos_detecs


def evaluate_detections(filepath):
    '''Evaluate face detections stored in a given filepath'''
    groupped_fnames = group_json_fnames(filepath=filepath)
    gold_fnames = groupped_fnames['gold']

    for idx, gold_fname in enumerate(gold_fnames):
        gold_json = load_json(os.path.join(filepath, gold_fname))
        for clsf in CLASSIFIERS:
            clsf_fname = groupped_fnames[clsf][idx]
            clsf_json = load_json(os.path.join(filepath, clsf_fname))
            gold_detection = get_rect_list(gold_json)
            clsf_detection = get_rect_list(clsf_json)

            tp, fp, fn, tp_dets = evaluate_detection(gold=gold_detection,
                                                     clsf_detection=clsf_detection)

            # dump evaluation data into a json file
            eval_json = {'classifier': clsf, 'true_positive': tp,
                         'false_positive': fp, 'false_negative': fn,
                         'true_positive_detections': tp_dets}

            eval_fname = clsf_fname[:-5] + '.eval.json'
            with open(os.path.join(filepath, eval_fname), 'w') as outfile:
                json.dump(obj=eval_json, fp=outfile, indent=4)


def main():
    '''main function'''
    classrooms = os.listdir(ROOT_DIR)
    for classroom in classrooms:
        dates = os.listdir(os.path.join(ROOT_DIR, classroom))
        for date in dates:
            filepath = os.path.join(ROOT_DIR, classroom, date)
            evaluate_detections(filepath=filepath)


if __name__ == "__main__":
    main()
