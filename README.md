# Predicting-School-Test-Scores

Data Source: https://www.kaggle.com/datasets/rkiattisak/student-performance-in-mathematics

Required Libraries: SQLite, pandas, numpy, matplotlib, seaborn, scikit-learn, and tensorflow.

Models Used: Linear & Logistic Regression, Random Forest, Decision Trees, K-Nearest Neighbors, Support Vector Regression, and Neural Network.


Model Optimization

In our first attempt to optimize the model, we created a simple model with two hidden layers and an outer layer. We started with dropping the math and reading scores to predict the writing score and converted the categorical data to numeric data with get dummies. We also split the preprocessed data into a features and target variable by identifying and dropping the writing score as the target variable. Then, we split the preprocessed data into a training and testing dataset and set the random state equal to 58. 

We further created a standard scaler to fit and scale the data. Then, we defined the model by creating two hidden layers. The first hidden layer was set equal to eight (8) with an activation set to “ReLU”. The second hidden layer was set equal to five (5) with an activation of “ReLU” as well. The output layer was set to a unit of one (1) with an activation of “Linear” since we are trying to solve a linear problem. The model was compiled with “loss “equal to “mean_squared_error”, optimizer equal to “adam” and metrics equal to “mse”. After training the model with one hundred (100) epochs, we got an r2 score of about 20%. We decided that this was a very low r2 score since the goal is at least 75%. Therefore, we decided to improve the model further trying other methods to get to a higher r2 score. 







![image](https://github.com/DanielPapp3/Predicting-School-Test-Scores/assets/68156846/45436a6e-2000-4818-b43f-41f0f8b70dce)

