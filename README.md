#  Uber and Lyft Price Prediction Based on Time and Weather Attributes (Case study: Boston, USA)

Uber and Lyft are the examples of ride-sourcing companies that use mobile app and work through connecting customers who are willing to pay for a ride with independent drivers who are willing to provide a ride 
with their privately-owned vehicles. 

## Project Purpose
Predicting uber and lyft potential prices based on the characteristic of weather and time. 

Presenting both of the prices in one simple app.

Providing some informations about what factors could affect price of uber/lyft in Boston.   



## Data and Method
This Project examines the efficiency of various regression models: LM, SVR, LGBM, Random Forest Regressor and XGBoost Regressor for predicting the price of Uber and Lyft. 

Data for 17 days (from  November  26th to  December 18th, 2018 in Boston) is downloaded from Kaggle dataset .


Independent Variable: Type of Car, Name of Car , Source, Distance,  Destination, Hour, Weekdays (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) are derived from the date/time factor, Wind, Rain, Temperature, Pressure, and Humidity

## Step
1. Data Prepocessing.                                                                                                                      
I converted column containing epoch time to actual datetime in car and weather dataset then merged both of them. There were missing values in price and rain columns, i decided to drop the missing values in price column since i cant compute manually and for rain columns i filled these missing values with zero value which indicate there was no rain on that day. 
I constructed new variables containing hour and day information from datetime variables for EDA purposes.Finally, I dropped some irrelevant data that isn't necessary and doesn't fit in the context of the problem that is trying to be solved

2. Feature Engineering.  
Since some algorithms can’t work with categorical data directly, Source, name ,day and hour columns that contain text values are need to be transformed to numerical values using one-hot encoding. 

3. Modelling

 
## Result

All models perform well and XGB Regressor with hyperparameter gives a minimum MAE amongst all models but i decided to choose Random Forest Regressor with hyperparameter. 


Name of car and distance are considered as the most significant variable for ride sharing price prediction in final model. 


![image](https://user-images.githubusercontent.com/60774724/83336314-a4d2ba80-a2dc-11ea-8a9c-6879dd813030.png)


