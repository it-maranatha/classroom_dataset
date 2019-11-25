# This Python script aims to form a summary table which aggregate the evaluation
# results  (stored as json files). The summary table is stored as csv file.

# import modules
import os
import csv
import json
from IBAtS_global import ROOT_DIR, CLASSIFIERS, load_json


def create_summary_table(fpath):
    '''Create a summary table (csv format) based on the evaluation files
    (json format)'''
    toCSV = []
    fnames = os.listdir(fpath)
    for fname in fnames:
        if not fname.startswith('[resize]') or not fname.endswith('.eval.json'):
            continue  # skip files other than evaluation files

        eval_json = load_json(os.path.join(fpath, fname))
        toCSV.append({'classifier': eval_json['classifier'],
                      'true_positive': eval_json['true_positive'],
                      'false_positive': eval_json['false_positive'],
                      'false_negative': eval_json['false_negative']})

    keys = toCSV[0].keys()
    with open('evaluation_summary.csv', 'a') as csv_file:
        dict_writer = csv.DictWriter(csv_file, keys)
        if os.stat('evaluation_summary.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerows(toCSV)


def main():
    '''main function'''
    with open('./evaluation_summary.csv', 'w') as my_empty_csv:
        # create an empty csv file
        pass

    classrooms = os.listdir(ROOT_DIR)
    for classroom in classrooms:
        dates = os.listdir(os.path.join(ROOT_DIR, classroom))
        for date in dates:
            fpath = os.path.join(ROOT_DIR, classroom, date)
            create_summary_table(fpath=fpath)


if __name__ == "__main__":
    main()
