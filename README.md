# Customer Sales Analytics

## Project Overview

This project analyzes customer sales data using Python and pandas to identify revenue patterns, customer behavior, product performance, regional performance, and monthly sales trends.

The project was developed as part of my Python and data analytics learning journey, with a focus on applying pandas to real-world business questions.

## Business Questions

The analysis explores questions such as:

* What is the company's total revenue?
* What is the average transaction value?
* Which products generate the most revenue?
* Which regions perform best?
* Which customers generate the most revenue?
* Who are the company's high-value customers?
* How concentrated is company revenue among top customers?
* Which products perform best across different months?
* Which regions perform best across different months?
* How does sales performance change over time?

## Dataset

The dataset contains 30 sales transactions with the following fields:

* **Customer** — Customer name
* **Region** — Customer's region
* **Product** — Product purchased
* **Quantity** — Number of units purchased
* **Unit_Price** — Price per unit
* **Sales** — Total transaction value
* **Month** — Month of the transaction

## Tools & Technologies

* Python
* pandas
* CSV
* Git & GitHub

## Analysis Techniques

The project applies:

* DataFrames and Series
* `pd.read_csv()`
* Data inspection and validation
* `groupby()`
* Aggregation with `.agg()`
* Filtering
* Sorting with `.sort_values()`
* Selecting top records with `.head()`
* Multi-level grouping
* Revenue-share calculations
* Customer and product analysis
* Regional and monthly analysis

## Key Business Insights

### Product Performance

Laptops generated the highest total sales and also had the highest average transaction value, while phones recorded the highest unit volume.

This suggests that laptops are particularly important for revenue generation, while phones contribute strongly to sales volume.

### Customer Performance

Michael generated the highest total revenue at **GHS 17,100**.

The analysis also showed that all customers made three transactions. Therefore, differences in customer revenue were driven primarily by transaction value rather than purchase frequency.

### High-Value Customers

Four customers met the project's high-value customer criteria:

* Michael
* Ama
* Daniel
* Kojo

The criteria were:

* Total sales above GHS 12,000
* Average transaction value above GHS 4,000

### Customer Revenue Concentration

The top three customers generated approximately **40.9%** of total company revenue.

This indicates some concentration among the highest-value customers, while the remaining revenue is still distributed across a broader customer base.

### Regional Performance

Accra generated the largest share of company revenue at approximately **42.6%**, followed by Kumasi at approximately **31.9%** and Takoradi at approximately **25.5%**.

Although Accra is the strongest region, revenue is distributed across all three regions rather than being entirely dependent on one market.

## Project Structure

```text
customer_sales_analytics/
│
├── customer_sales_analytics.py
├── sales.csv
└── README.md
```

## What I Learned

Through this project, I strengthened my ability to move from raw CSV data to structured business analysis using pandas.

I practiced:

* Loading and inspecting datasets
* Validating data
* Working with DataFrames
* Asking business questions using data
* Grouping and aggregating data
* Comparing customers, products, regions, and months
* Calculating revenue contribution
* Identifying high-value customers
* Translating analytical results into business insights

## Future Improvements

Potential future improvements include:

* Adding data visualizations
* Building an interactive dashboard
* Adding more customer segmentation
* Automating the analysis
* Expanding the dataset with additional transactions
* Adding monthly revenue trend visualizations

## Project Status

**Current version:** Customer sales analysis using Python and pandas.

This project demonstrates the transition from raw CSV data to structured business analysis and actionable insights.
