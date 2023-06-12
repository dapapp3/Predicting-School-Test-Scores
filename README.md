# Predicting-School-Test-Scores

Data Source: https://www.kaggle.com/datasets/rkiattisak/student-performance-in-mathematics

Required Libraries: SQLite, pandas, numpy, matplotlib, seaborn, scikit-learn, and tensorflow.

Models Used: Linear & Logistic Regression, Random Forest, Decision Trees, K-Nearest Neighbors, Support Vector Regression, and Neural Network.

## Introduction
Our project is based on a Kaggle dataset that sampled a group of 1,000 students and summarized their academic performance on 3 standardized tests: math, reading and writing while also providing additional interesting demographic information, such as gender, race/ethnicity, parental level of education, whether or not the student receives free lunch and whether or not the student completed a test prep course. We trained machine learning models using this dataset to attempt to predict what a student’s test scores would be using their other test scores as well as the demographic information.

## Model Optimization

In our first attempt to optimize the model, we created a simple model with two hidden layers and an outer layer. We started with dropping the math and reading scores to predict the writing score and converted the categorical data to numeric data with get dummies. We also split the preprocessed data into a features and target variable by identifying and dropping the writing score as the target variable. Then, we split the preprocessed data into a training and testing dataset and set the random state equal to 58. 

We further created a standard scaler to fit and scale the data. Then, we defined the model by creating two hidden layers. The first hidden layer was set equal to eight (8) with an activation set to “ReLU”. The second hidden layer was set equal to five (5) with an activation of “ReLU” as well. The output layer was set to a unit of one (1) with an activation of “Linear” since we are trying to solve a linear problem. The model was compiled with “loss “equal to “mean_squared_error”, optimizer equal to “adam” and metrics equal to “mse”. After training the model with one hundred (100) epochs, we got an r2 score of about 20%. We decided that this was a very low r2 score since the goal is at least 75%. Therefore, we decided to improve the model further trying other methods to get to a higher r2 score. 


