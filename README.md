# KKBOX's Churn Prediction

## Problem Statement

KKBOX is a music streaming service that mainly targets the markets of Asia. They offer a large and varied music library that contains 
over 30 million tracks. Since the service is working on a freemium basis, it is very crucial for the company to keep its paying
customers from canceling or not paying for their membership. 

Customer churn or customer default is a business problem that all companies have to deal with, and it is very important to have a solution
in place to reduce the churn rate and to also know the reasons behind why customers are leaving. 

Churn for KKBOX's use case is defined as follows:
> A churning customer is a subscribed customer that does not make a new subscription transaction within 30 days after the
> current membership expiration date.

By using different classification models, the goal is to accurately predict at any given month, the customers that will
churn in the next 30 days. The models are trained on previous user behavior calculated at different time windows to provide
the model with patterns and changes in each customer's behavior. 

Since some provided datasets are very large, I had to use other tools more adapted for Big Data to perform transformations and aggregations.
The data consists of time series values, so the temporal aspect of the data must be correctly handled in feature engineering 
and when doing training and cross-validation.

## Introduction
Enclosed in this folder, there can be found my analysis that I did to the real world
data provided by KKBox that contain their client's listening behavior as well as their personal information. I have used
Altair, Seaborn and Matplotlib for generating the graphs. As for the modeling part, I have used the following : **..complete me..**


### Motivation
The use of machine learning and data mining techniques has exploded during the last few years due the fact they enable
the business decisions takers to make wise decisions by taking into consideration the insights generated from them.

Music Streaming providers like KKBox could really benefit from integration data science techniques and generate more 
business value since the data collected from their clients is really informative.
You can find <a href="./eda.ipynb">here</a> the Exploratory Data Analysis for generating initial insights in regard to the behavior of churning 
clients and the difference between them and renewing clients. <br> 
The EDA step of the project is very important since it can point us at the right variables that are related to the churn 
rate of the clients. <br>


I have also made predictive models that are able to accurately predict which clients are more
likely to churn (not renewing their subscription within one month of their subscription's expiry date). <br>
You can find the notebook of the modeling phase <a href="#">here</a>.


Having access to both EDA and the predictive model is very useful for the company to make intelligent decisions 
about what they should do in order to keep their customers.

### Some Exploratory Data Analysis 

#### Preliminary Analysis: 

##### Churn distribution:

<p align="center"><img src="./images/churn_distribution.png" width=1200><p>


##### By Gender
<p align="center"><img src="./images/gender_churn.png" width=450><p>

##### By Age
<p align="center"><img src="./images/age.png" width=450><p>

##### By Tenure
<p align="center"><img src="./images/tenure.png" width=450><p>

##### By Amount Paid
<p align="center"><img src="./images/amount_paid.png" width=450><p>

##### By Number of Daily Transactions
<p align="center"><img src="./images/daily_transactions_number.png" width=1650 height=600><p>

##### By Number of Monthly Transactions
<p align="center"><img src="./images/monthly_transactions_number.png" width=1650 height=600><p>

##### By Auto Renew Feature
<p align="center"><img src="./images/auto_renew.png" width=450><p>

##### By Payment Method
<p align="center"><img src="./images/payment_method.png" width=450><p>

##### By Registration Method
<p align="center"><img src="./images/registration_method.png" width=450><p>

##### By Total Number of unique songs
<p align="center"><img src="./images/total_nbr_unique.png" width=450><p>

##### By Total Number of seconds listened
<p align="center"><img src="./images/total_seconds.png" width=450><p>