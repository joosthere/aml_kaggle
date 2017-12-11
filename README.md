# Kaggle Project for Applied Machine Learning

This is the repository for the 1<sup>st</sup> National Data Science Bowl Kaggle Challenge: Plankton Image Classification ([here](https://www.kaggle.com/c/1stdsbowl-in-class) or [here](https://www.kaggle.com/c/datasciencebowl)). This project was part of the Applied Machine Learning course for the MSc Information Studies at the University of Amsterdam ('17-'18).

## Goal

The goal of this project was to maximize test accuracy for the unknown labels of the `test_images`. In the original challenge the goal was to minimize Log Loss, but this was not the case for this project.

# Usage

## Required packages

All the required packages can be installed with either of the following commands:

```
pip install -r requirements.txt
pip3 install -r requirements.txt
```

## Structure

```
.
|-- data, all the Kaggle data files
	|-- images, contains any project related images
		|-- ...
	|-- label_map.txt, maps classes
	|-- sample.csv, contains sample of train_onelabel.csv
	|-- train_onelabel.csv
	|-- test_images, contains all the test images
		|-- *.jpg
	|-- train_images, contains all the train images
		|-- *.jpg, corresponds with the train_onelabel.csv
	|-- output
		|-- models, contains all the Keras Models
			|-- *.h5
		|-- predictions, contains all prediction files
			|-- *.csv
|-- notebooks
	|-- explore.ipynb (deprecated)
	|-- load_and_train.ipynb
	|-- load_and_predict.ipynb
	|-- load_and_predict_multiple.ipynb
	|-- preprocess.ipynb (deprecated)
	|-- Predictions.ipynb (deprecated)
```

For the sake of file size the Keras model files are not included in this repository. Please do note that the image folders are empty! Meaning that the train and test images are not present in this repository. This is, again, because of file sizes. However, the images are not large themselves, but they are with over 30.000 images in total.

## Notebooks

There are a few Jupyter Notebooks (or iPython if you will) in the repo and all are stored in `./notebooks`. Some are deprecated and are to be ignored, but the following are not:
* `load_and_train.ipynb`
* `load_and_predict.ipynb`
* `load_and_predict_multiple.ipynb`

They are, respectivally, to:
* load the `train_images` in a given format and to train a specific Convolution Neural Network architecture
* load a trained CNN model and to predict the classes of the `test_images`
* load multiple trained CNN models and combine their prediction of classes of the `test_images`

## Evaluation

Submissions were evaluated using the Category Accuracy. Each image had been labeled with one true class. For each image, we submitted our predicted class. The formula is then:

![accuracy](https://latex.codecogs.com/gif.latex?CategoryAccuracy%20%3D%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum_%7By_i%3D%5Chat%7By%7D_i%7D%5E%7Bn%7D1 "Category Accuracy Equation")

### Submission Format

We submitted csv files with the image name and the predicted class label. The order of the rows did not matter. The file needed to have a header and looked like the following:

```
image,class
1.jpg,0
10.jpg,99
...
etc
```