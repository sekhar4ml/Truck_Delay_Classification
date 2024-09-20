# **Build End-to-End ML Pipeline for Truck Delay Classification**
The project addresses a critical challenge faced by the logistics industry. Delayed truck shipments not only result in increased operational costs but also impact customer satisfaction. Timely delivery of goods is essential to meet customer expectations and maintain the competitiveness of logistics companies.
By accurately predicting truck delays, logistics companies can:
* Improve operational efficiency by allocating resources more effectively.
* Enhance customer satisfaction by providing more reliable delivery schedules.
* Optimize route planning to reduce delays caused by traffic or adverse weather conditions.
* Reduce costs associated with delayed shipments, such as penalties or compensation to customers.

## System Requirements

* python version : 3.10.2 or Later

## Library Requirements

* pymysql==1.1.0
* psycopg2==2.9.7
* pandas==1.5.3
* numpy==1.23.5
* matplotlib==3.7.1
* seaborn==0.12.2
* hopsworks==3.2.0

                                               ## **Approach**

  This Project develement has been devided into 3 different phases

  ** 1. Data Ingestion and Preparation
  ** 2. Machine Learning Model building & hyper perameter tunning 
  ** 3. Model Deploymnet and Inference


## **Data Ingestion and Preparation**

  This project is the first part of a three-part series aimed at solving the truck delay prediction problem. In this initial phase, we will utilize PostgreSQL and MYSQL in AWS Redshift to store the data, perform data retrieval, and conduct basic exploratory data analysis (EDA). With Hopsworks feature store, we will build a pipeline that includes data processing feature engineering and prepare the data for model building.
