# This Python script contains global identifiers/variables and functions

# import modules
import json

# define global identifiers
ROOT_DIR = './IBAtS_Initial_Dataset/'
CASCADE_DIR = './opencv/haarcascades/'
CLASSIFIERS = ['alt', 'al2', 'tre', 'def']
CLSF = {'alt': 'haarcascade_frontalface_alt.xml',
        'al2': 'haarcascade_frontalface_alt2.xml',
        'tre': 'haarcascade_frontalface_alt_tree.xml',
        'def': 'haarcascade_frontalface_default.xml'}
FACE_CLSF = 'haarcascade_frontalface_alt.xml'
NUMERALS = '0123456789abcdefABCDEF'
HEXDEC = {v: int(v, 16) for v in (x + y for x in NUMERALS for y in NUMERALS)}
NONPARTICIPANT_TAG = '#ff0000'


# define global functions
def load_json(fpath):
    '''Load json object from json file'''
    with open(fpath, 'r+') as json_file:
        json_obj = json.load(json_file)
    return json_obj


def rgb(triplet):
    return HEXDEC[triplet[0:2]], HEXDEC[triplet[2:4]], HEXDEC[triplet[4:6]]


def bgr(rgb_val):
    return rgb_val[2], rgb_val[1], rgb_val[0]
