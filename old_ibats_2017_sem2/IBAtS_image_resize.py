# This Python script aims to resize image files within the initial dataset

# import modules
import cv2
import os
from IBAtS_global import ROOT_DIR


def resize_image(fpath, max_axis=1024):
    '''Resize and save the resized image in the same directory.'''

    # load image file
    img = cv2.imread(fpath)

    # get image width and iamge height
    height, width = img.shape[:2]
    dim_long = max(width, height)

    # calculate new image width and image height
    r = max_axis / dim_long
    dim_resize = (0, 0)
    if dim_long == width:
        dim_resize = (max_axis, int(r * height))
    else:
        dim_resize = (int(r * width), max_axis)

    # resizing image
    img_resized = cv2.resize(img, dim_resize, interpolation=cv2.INTER_AREA)

    # save the resized image
    pathlist = fpath.split('/')
    fname = '[resize]{a}'.format(a=pathlist[-1])
    fname = os.path.join(*pathlist[:-1], fname)
    cv2.imwrite(fname=fname, img=img_resized)


def main():
    '''main function'''
    classrooms = os.listdir(ROOT_DIR)
    for classroom in classrooms:
        dates = os.listdir(os.path.join(ROOT_DIR, classroom))
        for date in dates:
            fnames = os.listdir(os.path.join(ROOT_DIR, classroom, date))
            for fname in fnames:
                if '.jpg' not in fname or '[resize]' in fname:
                    # skip non jpg files or resized jpg files
                    continue
                fpath = os.path.join(ROOT_DIR, classroom, date, fname)
                resize_image(fpath=fpath)


if __name__ == "__main__":
    main()
