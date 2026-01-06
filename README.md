# 🌾 Agricultural Crop Production & Yield Optimization Analytics System

## 📘 Abstract
Agricultural organizations generate large volumes of crop production data across regions, seasons, and crop types. However, fragmented data sources, manual analysis, and limited analytical capabilities often prevent timely and accurate decision-making.

This project presents an end-to-end agricultural analytics system that automates data ingestion, transformation, analytics, workflow orchestration, and visualization. Using Python, Databricks (PySpark), Apache Airflow, and Power BI, the system delivers actionable insights into crop production trends, yield optimization, and regional performance, enabling data-driven agricultural planning and policy formulation.



## 🎯 Project Objectives
The primary objectives of this project are to:
- Build a centralized analytics platform for agricultural data
- Automate ETL workflows using Apache Airflow
- Perform scalable transformations and analytics using PySpark
- Compute yield and productivity metrics accurately
- Provide interactive dashboards for stakeholders using Power BI
- Demonstrate real-world data engineering and analytics practices



## 🧰 Technology Stack

| Layer | Tools & Technologies |
|------|---------------------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Big Data Analytics | Databricks, PySpark |
| Workflow Orchestration | Apache Airflow |
| Data Storage | CSV, Delta Lake |
| Visualization | Power BI |
| Version Control | Git, GitHub |



## 📂 Project Structure
<pre>
├── data/
│   ├── raw/
│   │   ├── crop_production.csv
│   │   ├── market_prices.csv
│   │   ├── soil_health.csv
│   │   └── weather_data.csv
│   ├── bronze/
│   │   ├── bronze_crop_production.csv
│   │   ├── bronze_market_prices.csv
│   │   ├── bronze_soil_health.csv
│   │   └── bronze_weather.csv
│   ├── silver/
│   │   ├── silver_crop_production.csv
│   │   ├── silver_market_prices.csv
│   │   ├── silver_soil_health.csv
│   │   └── silver_weather.csv
│   └── gold/
│       ├── gold_agriculture_summary.csv
│       ├── gold_crop_weather_trend.csv
│       ├── gold_region_soil_yield.csv
│       └── gold_season_market_analysis.csv
├── notebooks/
│   ├── bronze_ingestion.ipynb
│   ├── silver_transformation.ipynb
│   └── gold_crop_production_trend.ipynb
├── airflow/
│   └── agriculture_pipeline.py
├── powerbi/
│   └── Capstone_Project.pbix
└── README.md
</pre>



## 📊 Data Description
The system processes multiple agricultural datasets, including:
- Crop Production Data – crop, state, district, year, season, area cultivated, and production
- Market Prices Data – crop-wise market price information
- Soil Health Data – soil quality and nutrient indicators
- Weather Data – rainfall and climatic attributes affecting yield

All datasets are ingested from raw CSV files and validated during the ingestion phase.



## 🏗️ Data Architecture: Bronze–Silver–Gold Model

### 🟤 Bronze Layer – Raw Data Ingestion
- Ingests raw CSV datasets into Databricks
- Performs schema validation and basic quality checks
- Stores data as Delta tables without transformations
Notebook: bronze_ingestion.ipynb

### ⚪ Silver Layer – Data Cleaning & Transformation
- Handles missing, null, and inconsistent values
- Standardizes crop names, seasons, and regional identifiers
- Converts columns to appropriate data types
- Calculates yield metrics (production per unit area)
Notebook: silver_transformation.ipynb

### 🟡 Gold Layer – Analytical Aggregations
- Crop-wise production trend analysis
- Seasonal yield performance evaluation
- Region-wise productivity comparison
- Year-over-year yield analysis
Notebook: gold_crop_production_trend.ipynb

![Agriculture Analytics Architecture](https://github.com/ashritham-23/Capstone_Project/blob/main/result_images/architecture.png)

## ⏱️ Workflow Automation using Apache Airflow
The complete ETL pipeline is orchestrated using Apache Airflow, ensuring reliable and automated execution.

Key DAG Features:
- Daily scheduled execution
- Retry mechanism for fault tolerance
- Clear task dependency: Bronze → Silver → Gold

DAG File: agriculture_pipeline.py

![Airflow automation](https://github.com/ashritham-23/Capstone_Project/blob/main/result_images/airflow_dag.png)

## 📈 Power BI Dashboards

### Dashboard Capabilities

1️⃣ Crop Production Overview
- Total crop production by crop type
- Year-wise production trends
- Season-wise production distribution

![Dashboard 1](https://github.com/ashritham-23/Capstone_Project/blob/main/result_images/dashboard_1.png)

2️⃣ Yield & Weather Performance
- Yield comparison across states and districts
- Identification of high-yield and low-yield regions
- Rainfall and climate impact on crop yield

![Dashboard 2](https://github.com/ashritham-23/Capstone_Project/blob/main/result_images/dashboard_2.png)

3️⃣ Soil & Market Impact Analysis
- KPI cards for production and yield metrics
- Soil health indicators vs yield performance
- Seasonal market price trends across crops

![Dashboard 3](https://github.com/ashritham-23/Capstone_Project/blob/main/result_images/dashboard_3.png)

Power BI File: Capstone_Project.pbix



## ✅ Testing & Validation

### Data Validation
- Missing value and null checks
- Schema and data type validation
- Yield calculation verification

### Analytical Validation
- Cross-verification of aggregated metrics
- Consistency checks across years and regions
- Dashboard values validated against Gold tables



## 🚀 How to Run the Project

1️⃣ Start Apache Airflow  
cd airflow  
docker compose up -d  

2️⃣ Access Airflow UI  
URL: http://localhost:8081  
Username: airflow  
Password: airflow  

3️⃣ Configure Databricks Connection  
Add `databricks_default` under Admin → Connections in Airflow UI  

4️⃣ Upload Raw Data to Databricks  
Upload crop_production.csv, market_prices.csv, soil_health.csv, and weather_data.csv to a Databricks Volume  

5️⃣ Initialize Database  
CREATE CATALOG agriculture_data;  

6️⃣ Execute the ETL Pipeline  
Trigger the agriculture_pipeline DAG and monitor execution in Airflow UI  

7️⃣ View Power BI Dashboard  
Open Capstone_Project.pbix in Power BI Desktop and refresh the data  


## 📦 Conclusion
- Built an end-to-end agricultural analytics system using the Bronze–Silver–Gold architecture.
- Automated ETL pipelines with Databricks, PySpark, and Apache Airflow.
- Delivered accurate analytics and insights through Power BI dashboards.
- Ensured data quality, scalability, and real-world data engineering practices.

## 🔮 Future Scope

### Real-Time Data Integration
The system can be enhanced by integrating real-time data sources such as weather APIs and government agricultural portals. This will enable continuous data updates and more timely insights for decision-makers.

### Predictive Analytics and Machine Learning
Machine learning models can be introduced to predict crop yield, assess production risks, and identify low-yield regions in advance. This will support proactive agricultural planning and resource allocation.

### Advanced Data Quality and Anomaly Detection
Anomaly detection techniques can be implemented to automatically identify unusual patterns or sudden drops in crop production and yield, improving data reliability and trust.

### Enhanced Visualization and Alerts
Power BI dashboards can be extended with real-time alerts, forecasting visuals, and drill-down capabilities to improve analytical depth and user interaction.

### Scalability and Platform Expansion
The pipeline can be scaled to handle larger datasets, additional regions, and more crop varieties. Support for mobile-friendly and multilingual dashboards can further improve accessibility for farmers and field officers.




### 👤  Author
Marumudi Ashritha 
