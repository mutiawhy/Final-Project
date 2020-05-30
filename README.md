##  Uber and Lyft Price Prediction Based on Time and Weather Attributes (Case study: Boston, USA)

Uber and Lyft are the examples of ride-sourcing companies that use mobile app and work through connecting customers who are willing to pay for a ride with independent drivers who are willing to provide a ride 
with their privately-owned vehicles. The price is volatile and affected by the demand and supply of rides at a given time. The first assumption of what drives the demand would be the time of the day; times around 9 am and 5 pm should see the highest surges on account of people commuting to work/home. Another assumption would be the weather; rain/snow should cause more people to take rides.

## Project Purpose
Predicting uber and lyft potential prices based on the characteristic of weather and time. 

Presenting both of the prices in one simple apps.

Providing some informations about what factors could affect price of uber/lyft in Boston.   



## Data

Data for 17 days (from  November  26th to  December 18th, 2018 in Boston) is downloaded from Kaggle dataset . The dataset consists of two files, these files are cab and weather dataset

The target variable : Price
The independent variable: Type of Car, Name of Car , Source, Distance,  Destination, Hour, Weekdays (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) are derived from the date/time factor, Wind, Rain, Temperature, Pressure, and Humidity

## Step
1. Data Prepocessing.                                                                                                                      
I have converted column containing epoch time to actual datetime in cab and weather dataset then merged both of them. There were missing values in price and rain columns, i decided to drop the missing values in price column since the price can't be computed randomly and for rain column, I filled the missing values with zero value which indicate there was no rain on that day. 
I constructed new variables containing hour and day information from datetime variables in this stage for EDA purposes. Finally, I dropped some irrelevant data that weren't necessary and didn't fit in the context of the problem that was trying to be solved

2. Feature Engineering.  
Since some algorithms can’t work with categorical data directly, Source, name ,day and hour columns that contain text values are need to be transformed to numerical values using one-hot encoding. I also used standarscaler to standardize the unit of some data.

3. Modelling.

I implemented various regression models: Linear Regression, SVR, LGBM, Random Forest Regressor, XGBoost Regressor and evaluated their performance on the test data and validation data using KFold. Hyperparameter tuning for the selected model has been done with the help of RandomizedSearchCV.

 
## Result

All models perform well and XGB Regressor with hyperparameter gives a minimum MA and RMSE amongst all models but { decided to choose Random Forest Regressor with hyperparameter. 


Name of car and distance are considered as the most significant variable for ride sharing price prediction in final model. 



##  This is how the machine learning model can be used on web app.
![image](https://user-images.githubusercontent.com/60774724/83336314-a4d2ba80-a2dc-11ea-8a9c-6879dd813030.png)





