# Denver-Behavioral-Health-Crime-Analysis

An end-to-end data analytics project clustering Denver zip codes to identify optimal intervention zones for behavioral health resources. 

## Project Overview
This project evaluates the relationship between local crime rates and the density of mental health and substance abuse treatment facilities. By leveraging unsupervised machine learning, the analysis groups neighborhoods into distinct "personas" to help city planners and stakeholders make data-driven funding and resource allocation decisions.

## Tech Stack
* **ETL Pipeline:** Python, Pandas, SQLite 
* **Statistical Analysis & Modeling:** R, K-Means Clustering, Multiple Linear Regression
* **Interactive Visualization:** Python, Streamlit, Plotly Express

## Key Insights (K-Means Personas)
Using K-Means clustering, the zip codes were segmented into three actionable profiles:
1. **Intervention Priority:** High violent crime rates but severely under-resourced in health and mental health facilities.
2. **Baseline:** The vast majority of Denver zip codes, featuring average crime and baseline facility density.
3. **Resource Hubs:** Areas with dense concentrations of health infrastructure. 

## How to Run the Dashboard Locally
1. Clone this repository.
2. Install the required dependencies:
   `pip install -r requirements.txt`
3. Launch the interactive dashboard:
   `streamlit run app.py`
