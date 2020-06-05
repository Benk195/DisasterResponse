# Disaster Response Pipeline Project

## Table of Contents
1. About the Project(#about)
2. [Installation](#installation)
3. [Author](#author)
5. [References](#ref)

<a name="about"></a>
## Summary

This project was set as part of the Udacity Nanodegree for Data Science. It hosts a machine learning classification model on a front-end web app as well as a few visualizations.

There are 3 distinct areas of the project. An ETL pipeline to process data coming from csv files, an ML pipeline to define and train the model; and finally a flask web-app to visualize the results.

<a name="installation"></a>
## Installation
The app uses Python 3.7, HTML and a small amount of Javascript

### Libraries
* nltk
* re
* pandas as pd
* numpy as np
* pickle
* sqlalchemy
* sklearn
* json
* plotly
* flask


### Installation
Clone the following GIT repository:

https://github.com/Benk195/DisasterResponse.git

### Running The Program

 - The ETL:
       `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
 - The ML:
       `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`
 - The App:
       `python run.py`

The go to http://0.0.0.0:3001/, to view the result

<a name="author"></a>
## Author

 - [Ben Kelly](https://github.com/Benk195)

<a name="ref"></a>
## Udacity

 - [Udacity](https://www.udacity.com/)
 - Thanks to Udacity for the support during this project