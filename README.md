# Healthcare Premium Prediction using Machine Learning

This project aims to develop a predictive model for Shield Insurance to estimate health insurance premiums based on factors such as age, smoking habits, BMI, and medical history.

## Project Objectives
The project’s core objectives are:

=> To develop a highly accurate predictive model that meets or exceeds a 97% accuracy threshold.
=> To ensure that predictions on at least 95% of cases have a percentage difference of less than 10% between predicted and actual values.
=>To deploy the model in a secure and scalable cloud environment, allowing Shield Insurance underwriters to use it remotely.
=>To create an intuitive Streamlit application for underwriters to easily input client data and receive premium estimates.
## Scope of Work (Phase 1: MVP Development)
### 1. Data Collection and Preprocessing
#### Data Collection: 
Gather labeled datasets containing essential features for premium prediction.
#### Data Cleaning : 
Handle missing values, outliers, and normalize/standardize data where necessary to ensure high-quality inputs for the model.
#### Exploratory Data Analysis (EDA): 
Conduct EDA to uncover data distributions, correlations, and significant predictive features.
### 2. Model Development
#### Model Selection: 
Experiment with various regression models (e.g., Linear Regression, Random Forest, Gradient Boosting) to find the most suitable algorithm.
#### Training and Evaluation: 
Train models and validate them using cross-validation to ensure robustness and prevent overfitting.
#### Hyperparameter Tuning:
Optimize model parameters to achieve target accuracy and minimize prediction error.
### 3. Model Deployment
#### Cloud Deployment: 
Deploy the optimized model on a cloud platform (e.g., AWS, GCP, or Azure) to enable remote access and high scalability.
#### Security Measures: 
Implement role-based access control and encryption to secure sensitive client data and ensure compliance with privacy standards.
### 4. Streamlit Application Development
#### User Interface: 
Design a clean, user-friendly interface that allows underwriters to enter client details, as shown in the screenshot below.



#### Functionality: 
Ensure that the app dynamically provides real-time predictions and displays detailed results for each input scenario.

### 5. Testing and Validation
#### Testing with Real-World Data: 
Validate model predictions using real-world data to ensure practical applicability and reliability.
#### Continuous Monitoring and Retraining: 
Set up a feedback loop to monitor the model's accuracy over time, ensuring it remains effective as new data becomes available.
### 6. Documentation and Training
#### Technical Documentation: 
Provide comprehensive documentation covering data pipeline, model selection, deployment steps, and Streamlit app functionality.
#### User Training: 
Prepare user guides or conduct live training sessions for insurance underwriters to ensure effective use of the application.
## Project Structure
The project files are organized as follows:

