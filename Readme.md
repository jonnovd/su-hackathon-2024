# SU Hackathon 2024
## by DeBuggers

## Problem Statement
With only an image of a pothole, we aim to predict the number of cement bags needed to fill the pothole.

## Usage
### Yolo
- Firstly the YoloV8 model is trained on the supplied training images by runnning train_model.py and correcting the path in pothole.yaml inside the Yolo folder.
- This model is used to predict the test annotations from the test images.

### Data preparation
- Run `merge_labels.py` in the merged_data folder to get only unique labels into train_labels.csv from the initial and supplementary data.
- Folders containing all images, annotations, and labels from the initial and supplementary data were placed here.

### code
- Scripts in this folder create the dataframes and csv files containing the features used to predict the number of bags in our prediction model.
- Run `extract_data.py` to get all complete entries of the training data into a csv file
- Run `pothole-area.py` to add the area of the potholes to this csv file
- Run `outlier_remover.py` to remove potholes with area outliers based on the bags used to fill the pothole
- The same process above must be followed for the test data, but `extract_test_data.py` should be run at the first step.
- This folder contains some other helper scripts that were used for the analysis of the data supplied to us

### Prediction Model
- `test_predictions.py` contains the code to train and run our SVR model for predicting the number of bags needed to fill the pothole
- The csv files generated from the previous step are used in this script
