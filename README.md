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

## PROJECT STRUCTURE

   ## **Approach**

  This Project develement has been devided into 3 different phases

  * 1. Data Ingestion and Preparation
  * 2. Machine Learning Model building & hyper perameter tunning 
  * 3. Model Deploymnet and Inference


## **Data Ingestion and Preparation**

  This project is the first part of a three-part series aimed at solving the truck delay prediction problem. In this initial phase, we will utilize PostgreSQL and MYSQL in AWS Redshift to store the data, perform data retrieval, and conduct basic exploratory data analysis (EDA). With Hopsworks feature store, we will build a pipeline that includes data processing feature engineering and prepare the data for model building.

### Data Ingestion Approach
 
* Upload truck delay training data into github repo
* Create MYSQL or Postgress DB Server ( move to AWS RDS in future)
* Create Truck_delays database and create tables for each of csv files
* Develop data_ingestion component to ingest data from github to MYSQL

### Data Exploration 

* Connect to Database
* Fetch Data from truck delay tables into Dataframes
* For each of the DataFrame -
  - Do basic checks of data ( info, describe, etc)
  - Chage Date column to datetime  ( ex : weather_df['date'] = pd.to_datetime(weather_df['date'])
* Data Analysis ( Important : For each of DF analyis - Clearly write your observations and recommandations)
  - Drivers
      * Histogram plots for numeric features
      * Scatter Plots ( Rating vs Average Speed)
      * Box Plot ( Driver Ratings by Gender)
  - Trucks
      * Histogram Plots for numeric features
      * Identify low milege Trucks and plot Trucks with age distribution
  - Routes
    * Histogram plots for numeric values
  - Traffic
    * Histogram plots for numeric values
    * Categorizes hours of the day into time periods.
      Example :
                if 300 <= hour < 600:
                       return 'Early Morning'

### Data cleaning

* For Each of the DataFrame
   - Identify and treat null values
   - Identify and treat outliers

### Feature Store

* Connect to feature store
* For each of the Data Frame,

  - Create event_time feature
      Example : drivers_df['event_time'] = pd.to_datetime('2024-09-19')
    
  - Create Feature group
    
               drivers_fg = fs.get_or_create_feature_group(
                   name="drivers_details_fg",                # Name of the feature group
                   version=1,                                # Version number
                   description="Drivers data",               # Description of the feature group
                   primary_key=['driver_id'],                # Primary key(s) for the feature group
                   event_time='event_time',                  # Event time column
                   online_enabled=False                      # Online feature store capability
               )
    
  - Insert DataFrame to feature group
    
                    drivers_fg.insert(drivers_df)
    
  - Create and Update Feature Group descriptions to each of the feature groups   
      
     
                  feature_descriptions_drivers = [
                  
                      {"name": "driver_id", "description": "unique identification for each driver"},
                      {"name": "name", "description": "name of the truck driver"},
                      {"name": "gender", "description": "gender of the truck driver"},
                      {"name": "age", "description": "age of the truck driver"},
                      {"name": "experience", "description": "experience of the truck driver in years"},
                      {"name": "driving_style", "description": "driving style of the truck driver, conservative or proactive"},
                      {"name": "ratings", "description": "average rating of the truck driver on a scale of 1 to 5"},
                      {"name": "vehicle_no", "description": "the number of the driver’s truck"},
                      {"name": "average_speed_mph", "description": "average speed of the truck driver in miles per hour"},
                      {"name": "event_time", "description": "dummy event time"}
                  
                  ]

                  for desc in feature_descriptions_drivers:
                      drivers_fg.update_feature_description(desc["name"], desc["description"])
                      

 - Configure statistics for the feature group

              # Configure statistics for the feature group
                  drivers_fg.statistics_config = {
                      "enabled": True,        # Enable statistics calculation
                      "histograms": True,     # Include histograms in the statistics
                      "correlations": True    # Include correlations in the statistics
                  }
                  
                  # Update the statistics configuration for the feature group
                  drivers_fg.update_statistics_config()
                  
                  # Compute statistics for the feature group
                  drivers_fg.compute_statistics()


  
