# Week 4: Analytics Engineering

# What is Analytics Engineering? and why is important in data science?

Analytics Engineering is a discipline that combines data analysis skills, software engineering, and project management to create scalable, reliable, and efficient data pipelines that allow companies to extract valuable insights from their data.

Analytics Engineering is important in data science because data is not useful if it cannot be collected, processed, and analyzed properly. Analytics engineers help create data infrastructure systems and automated workflows that enable companies to collect and process large amounts of data efficiently. Additionally, they also help create machine learning models and algorithms to analyze and visualize data, which enables companies to make informed, data-driven decisions.

In summary, Analytics Engineering is critical to data science as it focuses on designing and building systems and processes for the collection, storage, processing, and analysis of data. This enables companies to make informed, data-driven decisions, which can improve efficiency, productivity, and overall business outcomes.

# Question 1

Files:
[schema](hw_week4/staging/schema.yml)
[stg_green_tripdata.sql](hw_week4/staging/stg_green_tripdata.sql)
[stg_yellow_tripdata.sql](hw_week4/staging/stg_yellow_tripdata.sql)
[fact_trips.sql](hw_week4/core/fact_trips.sql)

```
SELECT count(1) 
FROM `raptor-land.dbt_fleal.fact_trips` 
where 
  extract(year from  pickup_datetime) between 2019 and 2020
```

61641974

# Question 2

data studio

- pie chart
- data range dimension: pickpup_datetime
- dimension: service type
- metric: record count

94/6

# Question 3

[schema](hw_week4/staging/schema.yml)
[stg_fhv_tripdata.sql](hw_week4/staging/stg_fhv_tripdata.sql)
[fact_fhv_trips.sql](hw_week4/core/fact_fhv_trips.sql)

```
dbt run --select stg_fhv_tripdata --var 'is_test_run: false'
```

43244696
	
# Question 4

22998722

# Question 5

[fact_fhv_trips_report.pdf](hw_week4/fact_fhv_trips_report.pdf)

January