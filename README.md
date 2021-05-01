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


