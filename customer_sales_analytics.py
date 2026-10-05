# Create the csv file and upload the 30 rows of data 
import csv
with open("sales.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Customer","Region","Product","Quantity","Unit_Price","Sales","Month"])
    rows = [
    ["Gifty", "Accra", "Laptop", 1, 4500, 4500, "January"],
    ["Ama", "Kumasi", "Phone", 2, 1500, 3000, "January"],
    ["Michael", "Takoradi", "Monitor", 2, 1800, 3600, "January"],
    ["Sarah", "Accra", "Tablet", 1, 1800, 1800, "February"],
    ["Kwame", "Accra", "Phone", 3, 1500, 4500, "February"],
    ["Daniel", "Kumasi", "Laptop", 1, 5000, 5000, "February"],
    ["Abena", "Accra", "Phone", 2, 1500, 3000, "March"],
    ["Kojo", "Takoradi", "Tablet", 2, 1800, 3600, "March"],
    ["Linda", "Kumasi", "Phone", 1, 1800, 1800, "March"],
    ["Joseph", "Accra", "Laptop", 1, 4200, 4200, "March"],
    ["Gifty", "Accra", "Monitor", 1, 2000, 2000, "April"],
    ["Ama", "Kumasi", "Laptop", 2, 4500, 9000, "April"],
    ["Michael", "Takoradi", "Phone", 3, 1500, 4500, "April"],
    ["Sarah", "Accra", "Phone", 1, 1600, 1600, "May"],
    ["Kwame", "Accra", "Laptop", 1, 4500, 4500, "May"],
    ["Daniel", "Kumasi", "Monitor", 2, 1800, 3600, "May"],
    ["Abena", "Accra", "Tablet", 2, 1800, 3600, "June"],
    ["Kojo", "Takoradi", "Laptop", 1, 5000, 5000, "June"],
    ["Linda", "Kumasi", "Tablet", 1, 1800, 1800, "June"],
    ["Joseph", "Accra", "Phone", 2, 1500, 3000, "June"],
    ["Gifty", "Accra", "Tablet", 1, 1800, 1800, "July"],
    ["Ama", "Kumasi", "Monitor", 2, 2000, 4000, "July"],
    ["Michael", "Takoradi", "Laptop", 2, 4500, 9000, "July"],
    ["Sarah", "Accra", "Laptop", 1, 4500, 4500, "August"],
    ["Kwame", "Accra", "Monitor", 1, 2000, 2000, "August"],
    ["Daniel", "Kumasi", "Phone", 3, 1500, 4500, "August"],
    ["Abena", "Accra", "Laptop", 1, 5000, 5000, "September"],
    ["Kojo", "Takoradi", "Monitor", 2, 2000, 4000, "September"],
    ["Linda", "Kumasi", "Laptop", 1, 4500, 4500, "September"],
    ["Joseph", "Accra", "Tablet", 2, 1800, 3600, "September"]
    ]
    for row in rows:
        writer.writerow(row)

# Import the dataset into pandas 
import pandas as pd
sales = pd.read_csv("sales.csv")

# Validate the data 
sales.shape
sale.columns
sales.head()
sales.dtypes 
sales.isnull().sum()
sales.describe()

# Total revenue
sales["Sales"].sum()

# Total units sold
sales["Quantity"].sum()

# Average transaction value
sales["Sales"].mean()

# Number of transactions
sales["Sales"].count()

# Which products are driving the business?
# Using groupby(), calculate for each product:

# Total units sold
sales.groupby("Product")["Quantity"].sum()

# Total sales
sales.groupby("Product")["Sales"].sum()

# Average transaction value
sales.groupby("Product")["Sales"].mean()

# Use named aggregation to create a clean business summary.
sales.groupby("Product").agg(
     Total_Units_Sold = ("Quantity","sum"),
     Total_Sales = ("Sales","sum"),
     Average_Transaction_Value = ("Sales","mean")
     )

# Which region is contributing the most to the business?
# Using groupby() and .agg(), create one summary table for each region containing:
# Total units sold
# Total sales
# Average transaction value
sales.groupby("Region").agg(
    Total_Units_Sold = ("Quantity","sum"),
    Total_Sales = ("Sales","sum"),
    Average_Transaction_Value = ("Sales","mean")
    )

# How did sales performance change across the months?
sales.groupby("Month").agg(
     Total_Units_Sold = ("Quantity","sum"),
    Total_Sales = ("Sales","sum"),
    Average_Transaction_Value = ("Sales","mean")
     )

# Create a summary grouped by both Region and Product.
# For each Region–Product combination, calculate:
# Total units sold
# Total sales
# Average transaction value
sales.groupby(["Region","Product"]).agg(
    Total_Units_Sold = ("Quantity","sum"),
    Total_Sales = ("Sales","sum"),
    Average_Transaction_Value = ("Sales","mean")
    )

# Which customer has generated the most revenue for the business?
Customer_total_sales = sales.groupby("Customer")["Sales"].sum()
Customer_total_sales.sort_values(ascending=False)
# OR
sales.groupby("Customer")["Sales"].sum().sort_values(ascending=False)

# What percentage of the company's total revenue comes from each customer?
(sales.groupby("Customer")["Sales"].sum()/sales["Sales"].sum()*100).rename("Customer_Revenue_Share").sort_values(ascending=False)

# Which customers make the most purchases, and are the most frequent customers also the highest-revenue customers?
sales.groupby("Customer").agg(
    Total_Sales = ("Sales","sum"),
    Number_of_Transactions = ("Customer","count"),
    Average_Transaction_Value = ("Sales","mean")).sort_values("Total_Sales",ascending=False)

# Let's define a high-value customer for this exercise as someone who:
# has Total Sales greater than GHS 12,000, AND
# has an Average Transaction Value greater than GHS 4,000
customer_summary = sales.groupby("Customer").agg(
    Total_Sales = ("Sales","sum"),
    Number_of_Transactions = ("Customer","count"),
    Average_Transaction_Value = ("Sales","mean")).sort_values("Total_Sales",ascending=False)
customer_summary[(customer_summary["Total_Sales"]>12000) &
                 (customer_summary["Average_Transaction_Value"]>4000)
                 ]

# Using customer_summary, calculate the percentage of total company revenue generated by the top 3 customers combined
customer_summary["Total_Sales"].head(3).sum()/customer_summary["Total_Sales"].sum()*100

# Create a summary grouped by both Customer and Product, showing:
# Total units sold
# Total sales
# Average transaction value
customer_product_summary = sales.groupby(["Customer","Product"]).agg(
    Total_Units_Sold = ("Quantity","sum"),
    Total_Sales = ("Sales","sum"),
    Average_Transaction_Value = ("Sales","mean")
    )

# Using customer_product_summary, find the top 5 customer-product combinations by Total Sales
customer_product_summary.sort_values("Total_Sales",ascending=False).head(5)

# Using the original sales DataFrame, create a monthly summary containing:
# Total Units Sold
# Total Sales
# Average Transaction Value
# Group by Month
sales.groupby("Month").agg(
    Total_Sales = ("Sales","sum"),
    Total_Units_Sold = ("Quantity","sum"),
    Average_Transaction_Value = ("Sales","mean")).sort_values("Total_Sales",ascending=False)

# Which region generated the most sales in each month?
sales.groupby(["Month", "Region"]).agg( 
    Total_Sales=("Sales", "sum"),
    Total_Units_Sold=("Quantity", "sum"),
    Average_Transaction_Value=("Sales", "mean")
).sort_values("Total_Sales", ascending=False).groupby("Month").head(1)
