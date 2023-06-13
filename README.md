# Predicting-School-Test-Scores

Data Source: https://www.kaggle.com/datasets/rkiattisak/student-performance-in-mathematics

Required Libraries: SQLite, pandas, numpy, matplotlib, seaborn, scikit-learn, and tensorflow.

Models Used: Linear & Logistic Regression, Random Forest, Decision Trees, K-Nearest Neighbors, Support Vector Regression, and Neural Network.

## Introduction
Our project is based on a Kaggle dataset that sampled a group of 1,000 students and summarized their academic performance on 3 standardized tests: math, reading and writing while also providing additional interesting demographic information, such as gender, race/ethnicity, parental level of education, whether or not the student receives free lunch and whether or not the student completed a test prep course. We trained machine learning models using this dataset to attempt to predict what a student’s test scores would be using their other test scores as well as the demographic information.

## Model Optimization

In our first attempt to optimize the model, we created a simple model with two hidden layers and an outer layer. We started with dropping the math and reading scores to predict the writing score and converted the categorical data to numeric data with get dummies. We also split the preprocessed data into a features and target variable by identifying and dropping the writing score as the target variable. Then, we split the preprocessed data into a training and testing dataset and set the random state equal to 58. 

We further created a standard scaler to fit and scale the data. Then, we defined the model by creating two hidden layers. The first hidden layer was set equal to eight (8) with an activation set to “ReLU”. The second hidden layer was set equal to five (5) with an activation of “ReLU” as well. The output layer was set to a unit of one (1) with an activation of “Linear” since we are trying to solve a linear problem. The model was compiled with “loss “equal to “mean_squared_error”, optimizer equal to “adam” and metrics equal to “mse”. After training the model with one hundred (100) epochs, we got an r2 score of about 20%. We decided that this was a very low r2 score since the goal is at least 75%. Therefore, we decided to improve the model further trying other methods to get to a higher r2 score. 

## Visualizations

![image](https://github.com/DanielPapp3/Predicting-School-Test-Scores/assets/95590929/845b8930-ff5d-489a-8fef-3ef3c25ea73e)

The heat map shows us that there is a strong correlation between a student’s score on one exam, and all of their other exams, especially for reading and writing scores. There is a 95% correlation between a reading and writing score, meaning if a student scores very highly on their writing exam, they almost always performed well on their reading exam as well.


![image](https://github.com/DanielPapp3/Predicting-School-Test-Scores/assets/95590929/f3a8d804-89f1-4624-a10b-b3a2062fcf77)

In the following cat plots, we found that there isn’t a lot variability in our data when looking at the parental level of education. However, in the cat plot on the right, “math scores vs race/ethnicity”, we can see that there is one race/ethnicity that sticks out as closer to the top, the male, group E demographic.

![image](https://github.com/DanielPapp3/Predicting-School-Test-Scores/assets/95590929/760e8117-b8d1-4fe5-84f8-206d654bcc98)

This last visualization is very similar to the heat plot; the reading and writing scores have a very high correlation as the data points are more closely packed together on the line while the math score has a slightly weaker correlation to the writing scores.

## Conclusion

In conclusion, using demographic data points only to predict the scores does not yield good results, so it’s not enough to make a prediction. The highest R-squared score from using demographic points only was for the writing score which was 0.343, which isn’t close to enough. This means that the best predictor for test scores in one subject are test scores in other subjects. The predictions are even better when you use both the demographic data and the test score data and this is further proven to being a good predictor for the model by the fact that the root mean squared (RMS) error, 3.83, is lower than the standard deviation, 15.02, of the target variable.
