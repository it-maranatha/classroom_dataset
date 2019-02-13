# FACE - Face At Classroom Environment
This is the public repository for FACE - Face At Classroom Environment.
We made this repository publicly available along with our published conference paper [IEEE IPTA](https://doi.org/10.1109/IPTA.2018.8608166)].

The repository contains gold standard image dataset of students sitting in the laboratory classroom environment.
Tools and scripting to pre-process and to analyse the dataset are included in the repository.
We plan to maintain the dataset by continuously adding new data to the repository.

Our dataset could be utilised in several different studies.
The most prominent one is in the study of face detection/recognition, especially when classrooms are the environment of interest.
Researchers could evaluate their proposed method against our gold standard dataset.
Moreover, studies in computer vision targeted automated student attendance systems would be benefit from our dataset.
A more general study in face detection/recognition and other study in educational data mining could also take advantage of the dataset.

We welcome researchers and other interested parties across the globe to take advantage of the dataset.
If you need to refer to our dataset for your scientific publication you can do it by citing our conference paper.

Following are brief information regarding the repository:

## Image dataset
Our image dataset is accessible via this [link](https://github.com/itmaranatha/classroom_dataset/tree/master/IBAtS_Initial_Dataset).
The dataset is grouped into several different course codes (e.g., BS301, IN010, or IX801).
For each course code, the dataset is further grouped into several different date which represent the date when the images were taken.
Each image is resized and stored as JPG file with file naming ``[resize]xx.jpg``, where xx is an incremental integer number (e.g., ``[resize]01.jpg`` or ``[resize]02.jpg``).
Each image file is accompanied by a meta-data stored as JSON file with file naming similar to the image file name except for the extension of the file which is ``.gold.json`` (e.g., ``[resize]01.gold.json`` or ``[resize]02.gold.json``).
Such meta-data is manually crafted, each represent the annotation of faces' location contained within a given image.
These images with their gold meta-data form a gold standard dataset.

## Image resizing
Each image in this repository is resized with 1,024
pixels as its widest size.
A simple Python script ([IBAtS_image_resize.py](https://github.com/itmaranatha/classroom_dataset/blob/master/IBAtS_image_resize.py)) is written to automate the job.

## Image tagging
As mentioned in our paper, image tagging/labeling is a highly laborious task.
We tried to lighten the work-load by partially automating the task.
The gold meta-data in this repository was formed in two-folds:

- First,  a pre-trained classifier was employed to locate faces in every image.
For this purpose, a simple Python script is written ([IBAtS_face_detection.py](https://github.com/itmaranatha/classroom_dataset/blob/master/IBAtS_face_detection.py)).
- Second, each image is further iteratively inspected and manually corrected (in the case where false detection is present).
For this purpose, a Jupyter Notebook script and a simple Java GUI application are built ([IBAtS_gold_standard_visualiser.ipynb](https://github.com/itmaranatha/classroom_dataset/blob/master/IBAtS_gold_standard_visualiser.ipynb), [IBATS_image_tagger.jar](https://github.com/itmaranatha/classroom_dataset/blob/master/IBATS_image_tagger.jar)).

## Data cleansing
Data cleansing is mainly dealing with exclusion of non-participants from the dataset.
This is done by manually change the tag colour (i.e., rectangle colour) for each non-participant to red using the same Java GUI application that was used to conduct manual image tagging ([IBATS_image_tagger.jar](https://github.com/itmaranatha/classroom_dataset/blob/master/IBATS_image_tagger.jar)).
Further, each face with red colour mark will be covered with a filled rectangle.
A simple Python script is written to automate this process ([IBAtS_data_cleansing.py](https://github.com/itmaranatha/classroom_dataset/blob/master/IBAtS_data_cleansing.py)).

## Classifier evaluation
Four pre-trained classifiers are evaluated in this repository, where the gold standard dataset is used as the baseline for the evaluation.
These pre-classifiers are publicly accessible within the [OpenCV library](https://github.com/opencv/opencv).
A simple Python script is written to automate the process ([IBAtS_face_detection_four_classifiers.py](https://github.com/itmaranatha/classroom_dataset/blob/41024d669c4067f77176aacf61dac3d470c6e555/IBAtS_face_detection_four_classifiers.py)).

## Qualitative analysis
Qualitative analysis is conducted by manually assessing the automated detected faces yielded by each pre-trained classifier.
A simple Jupyter Notebook script is written to assist the procedure ([IBAtS_classifier_evaluation_visualiser.ipynb](https://github.com/itmaranatha/classroom_dataset/blob/41024d669c4067f77176aacf61dac3d470c6e555/IBAtS_classifier_evaluation_visualiser.ipynb)).

## Quantitative analysis
Quantitative analysis is conducted by first counting the number of true positive, false positive, and false negative detections yielded by each pre-trained classifier.
Two Python scripts are written to serve this purpose ([IBAtS_classifier_evaluation.py](https://github.com/itmaranatha/classroom_dataset/blob/41024d669c4067f77176aacf61dac3d470c6e555/IBAtS_classifier_evaluation.py) and [ 	IBAtS_evaluation_summary_table.py](https://github.com/itmaranatha/classroom_dataset/blob/41024d669c4067f77176aacf61dac3d470c6e555/IBAtS_evaluation_summary_table.py)).
Further, some data visualisations are generated to assist the quantitative analysis.
For this purpose, a Jupyter Notebook script is written ([IBAtS_quantitative_data_analysis.ipynb](https://github.com/itmaranatha/classroom_dataset/blob/41024d669c4067f77176aacf61dac3d470c6e555/IBAtS_quantitative_data_analysis.ipynb)).
