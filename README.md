## Test Project : https://kunnalpatil-data-science-salary--estimator-wiykfc.streamlit.app/
# Data Science Salary Estimator: Project Overview
* Created a salary Estimator for data science job roles using data from glassdoor.
* Engineered features from the text of each job description to quantify the salaries <br>
companies put on python, excel, aws, and spark.
* Optimized Lasso Regession and RandomForestRegressors using RandomsearchCV to reach the best model.
* Finally deployed the project on heruko.
# Packages used: 
 pandas, numpy, sklearn, matplotlib, seaborn,pickle.
 
# Data Cleaning:
After getting the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

* Parsed numeric data out of salary
* Made columns for employer provided salary and hourly wages
* Removed rows without salary
* Parsed rating out of company text
* Made a new column for job state
* Added a column for if the job was at the company’s headquarters
* Transformed founded date into age of company
* Made columns for if different skills were listed in the job description:
  * Python
  * R
  * Excel
  * AWS
  * Spark
* Column for simplified job title and Seniority
* Column for description length

# EDA 
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.
### Correlation matrix
![image](https://user-images.githubusercontent.com/88432965/166195596-9d583622-d19d-46e1-9a91-79757e9e2f69.png)

The Description of job and age of company are highly correlated.
older companies have more competitors.

### graph for Sector and job roles
![image](https://user-images.githubusercontent.com/88432965/166195859-44472c49-c63a-4d64-b945-894cba794473.png)
![image](https://user-images.githubusercontent.com/88432965/166195953-e952a924-0218-4460-b62f-be1cdff07b46.png)

# Model Building
First, I transformed the categorical variables into dummy variables. I also split the data <br>
into train and tests sets with a test size of 20%.

I tried two different models:
 * Lasso Regression : cause it normalizes the data for prediction 
 * RandomForestRegressor

# Model performance

Random Forest:MAE = 13.69 <br>
Lasso Regression:NMAE = -22.86
