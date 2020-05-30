#  Uber and Lyft Price Prediction Based on Time and Weather Attributes (Case study: Boston, USA)

Uber and Lyft are the examples of ride-sourcing companies that use mobile app and work through connecting customers who are willing to pay for a ride with independent drivers who are willing to provide a ride 
with their privately-owned vehicles. 

## Project Purposes
Predict uber and lyft potential prices based on the characteristic of weather and time. 

Get to know both of the prices from one simple app.

Give some informations about what factors could affect price of uber/lyft in Boston.   



## Data and Method
This Project examines the efficiency of various regression models: LM, SVR, LGBM, Random Forest Regressor and XGBoost Regressor for predicting the price of Uber and Lyft. 

Data for 17 days (from  November  26th to  December 18th, 2018 in Boston) is downloaded from Kaggle dataset .


Independent Variable: Type of Car, Name of Car , Source, Distance,  Destination, Hour, Weekdays (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) are derived from the date/time factor, Wind, Rain, Temperature, Pressure, and Humidity

 
## Result

All models perform well and XGB Regressor with hyperparameter gives a minimum MAE amongst all models but i decided to choose Random Forest Regressor with hyperparameter. 


Name of car and distance are considered as the most significant variable for ride sharing price prediction in final model. 
 

